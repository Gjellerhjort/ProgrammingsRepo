library ieee;
use ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;


entity UART_RX is
generic (
    g_CLKS_PER_BIT : integer := 3333     -- Needs to be set correctly
    );
  port (
    I_Clk       : in  std_logic;
    i_RX_Serial : in std_logic;
    o_RX_DV     : out std_logic;
    o_RX_Byte   : out std_logic_vector(7 downto 0)
    );
end UART_RX;

architecture Behavioral of UART_RX is

  --------------- UART ---------------
  type t_SM_Main is (s_Idle, s_RX_Start_Bit, s_RX_Data_Bits, s_RX_Data_Bits_Extra,
                     s_RX_Stop_Bit, s_Cleanup);
  signal r_SM_Main : t_SM_Main := s_Idle;
 
  signal r_RX_Data_R : std_logic := '0';
  signal r_RX_Data   : std_logic := '0';
  
  signal r_Clk_Count : integer range 0 to g_CLKS_PER_BIT-1 := 0;
  signal r_Bit_Index : std_logic_vector(2 downto 0) := (others => '0');
  signal r_RX_Byte   : std_logic_vector(7 downto 0) := (others => '0');
 
  signal r_RX_DV     : std_logic := '0';
  
  signal UART_IN: std_logic_vector (10 downto 0):= (others => '0'); -- til PROGRAM
  
  --------------- PROGRAM ---------------
  type rom_type is array (0 to 3) of std_logic_vector (15 downto 0);
  signal PROGRAM : rom_type :=(X"0000",X"0000",X"0000",X"0000");
  signal PC : STD_LOGIC_VECTOR (8 downto 0):="000000000";
  signal rdata : STD_LOGIC_VECTOR (15 downto 0);
  signal slow_clk: STD_LOGIC;
  signal clk_cnt: STD_LOGIC_VECTOR (20 downto 0):=(others => '0');
  signal regA : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Current Sensor Data
  signal regB : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Ønskede temperatur
  signal regiA : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Current Sensor Data
  signal regiB : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Ønskede temperatur
  signal regC : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Resultat fra ALU
  signal regD : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Data register til flytning
  signal regE : STD_LOGIC_VECTOR (3 downto 0):="0000"; -- Ingen af delerne er valgt af casen og bliver udskrevet "Error Case"
  signal cnt : STD_LOGIC_VECTOR (3 downto 0):="0000";
  signal i: STD_LOGIC := '0';
  signal OP_CODE: std_logic_vector (7 downto 0);	
  signal result: std_logic_vector (7 downto 0);
  signal saveReg: std_logic_vector (7 downto 0):=(others => '0');
  
  --
begin
 
  -- Purpose: Double-register the incoming data.
 -- This allows it to be used in the UART RX Clock Domain.
  -- (It removes problems caused by metastabiliy)
  o_RX_DV <= r_RX_Data; -- for oscilloscop check
  p_SAMPLE : process (I_Clk)
  begin
    if rising_edge(I_Clk) then
      r_RX_Data_R <= i_RX_Serial;
      r_RX_Data   <= r_RX_Data_R;
          
    end if;
  end process p_SAMPLE;
  
  process (I_clk)
    begin
        if (I_clk'event and I_clk = '1') then
            clk_cnt <= clk_cnt + 1;
	    end if; 
   end process;
	
	slow_clk <= clk_cnt(0);
--	WA <= rdata;
--	WB <= regA;
--	WC <= regB;
--	WD <= OP_CODE;
-- LED <= regC;	
  
  -- Purpose: Control RX state machine 
  p_UART_RX : process (I_Clk)
  begin
 
    if rising_edge(I_Clk) then
        
       case r_SM_Main is
 
        when s_Idle =>
          --r_RX_DV     <= '0';
          r_Clk_Count <= 0;
          r_Bit_Index <= "000";
 
          if r_RX_Data = '0' then       -- Start bit detected
            r_SM_Main <= s_RX_Start_Bit;
                      --r_Bit_Index <= 1;
          else
            r_SM_Main <= s_Idle;
                     
          end if;
           
        -- Check middle of start bit to make sure it's still low
        when s_RX_Start_Bit =>
          if r_Clk_Count = (g_CLKS_PER_BIT-1)/2 then
            if r_RX_Data = '0' then
              r_Clk_Count <= 0;  -- reset counter since we found the middle
              r_SM_Main   <= s_RX_Data_Bits;
            else
              r_SM_Main   <= s_Idle;
            end if;
          else
            r_Clk_Count <= r_Clk_Count + 1;
            r_SM_Main   <= s_RX_Start_Bit;
          end if;
          
        -- Wait g_CLKS_PER_BIT-1 clock cycles to sample serial data
        when s_RX_Data_Bits =>
          if r_Clk_Count < g_CLKS_PER_BIT-1 then
            r_Clk_Count <= r_Clk_Count + 1;
            r_SM_Main   <= s_RX_Data_Bits;
          else
            r_Clk_Count <= 0;
            r_RX_Byte(conv_integer(r_Bit_Index)) <= r_RX_Data;
				UART_IN(8 downto 1) <= r_RX_Byte;
            r_SM_Main   <= s_RX_Data_Bits_Extra;
          end if;
           
            --Check if we have sent out all bits
          when s_RX_Data_Bits_Extra =>
            if r_Bit_Index < 7 then
              r_Bit_Index <= r_Bit_Index + 1;
              r_SM_Main   <= s_RX_Data_Bits;
            else
              r_Bit_Index <= "000";
              r_SM_Main   <= s_RX_Stop_Bit;
            end if;
 
        -- Receive Stop bit.  Stop bit = 1
        when s_RX_Stop_Bit =>
          -- Wait g_CLKS_PER_BIT-1 clock cycles for Stop bit to finish
          if r_Clk_Count < g_CLKS_PER_BIT-1 then
             r_Clk_Count <= r_Clk_Count + 1;
             r_SM_Main   <= s_RX_Stop_Bit;
          else
            r_RX_DV     <= '1';
            r_Clk_Count <= 0;
            r_SM_Main   <= s_Cleanup;
          end if;
                  
        -- Stay here 1 clock
        when s_Cleanup =>
          r_SM_Main <= s_Idle;
          r_RX_DV   <= '0';
 
          when others =>
          r_SM_Main <= s_Idle;
          
      end case;
    end if;
  end process p_UART_RX;
  
   process (slow_clk)
  begin
--  rdata <= PROGRAM(conv_integer(PC));
--  PROGRAM(0)(14 downto 6) <= "100000011";-- A
--  PROGRAM(1)(14 downto 6) <= "010000111";-- B
--  PROGRAM(2)(14 downto 6) <= "001001111";-- C
--  PROGRAM(3)(14 downto 6) <= "000000000";
	
			 if rising_edge(slow_clk) then
							  OP_CODE <= r_RX_Byte;
							 
							  case OP_CODE(7) is
								  when '1' =>
								  regA(2 downto 0) <= OP_CODE(6 downto 4);
								  regB <= OP_CODE(3 downto 0);
								  result <= OP_CODE;
								  PROGRAM(0)(14 downto 11) <= regA;
								  PROGRAM(0)(10 downto 7) <= regB;
								  result <= PROGRAM(0)(14 downto 7);
								  saveReg <= result;
								  
								  when '0' =>
								  result(7 downto 4) <= regA;
								  result(3 downto 0) <= regB;
								  -- burde give samme resultat som ovenover???

								  
								  when others => result <= "11111111";
								  end case;
							  
								
--							  IGNORER DEBUG
							  
--							  When "00000011" =>
--							  result <= "00000010";
--							  
--							  When "00100011" =>
--							  result <= "00100011";
--							  
--							  When "00001110" => 
--							  result <= "00000010";
--							  -- Sensor --
--							  --regC <= std_logic_vector(unsigned(regA) + unsigned(regB));
--							  
--							  When "00010000" =>
--							  result <= "00000100";
--
--							  When "01000000" =>
--							  result <= "00001000";
--							  
--							  When "11111111" =>
--							  result <= "10000000";
							  
--							  When "11111" =>
----							  regC <= "1001";
----							  result(3 downto 0) <= regC;
--							  --When "00001" =>
--							  --regC <= std_logic_vector(unsigned(regA) + unsigned(regB));
--							  When "00010" =>
--							  --regC <= std_logic_vector(unsigned(regA) + unsigned(regB));
--							  When "00011" =>
--							  --regC <= std_logic_vector(unsigned(regA) - unsigned(rdata));
--							  
--							  when "10000" => regA <= PROGRAM(0)(9 downto 6);
--							  when "01000" => regB <= PROGRAM(1)(9 downto 6);
--							  --when "10000" => regC <= PROGRAM(2)(9 downto 6);
--							  
--							  when others => 
--							  -- Ud på 7-Segment <= regE; 
--							  end case;
							  		
						if PC < 4 then
							PC <= PC + 1;
							--LED_SEG_out <= PC;
							elsif PC >= 4 then
								PC <= "000000000";
					   end if;
			 end if;    
			 
	end process;
 
  --o_RX_DV <= r_RX_DV;
  o_RX_Byte <= result;
  
  
end Behavioral;

