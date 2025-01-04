----------------------------------------------------------------------------------
-- Company: AAU
-- Engineer: Henrik Schi�ler
--
-- Create Date: 06/26/2023 04:21:46 PM
-- Design Name:
-- Module Name: top - Behavioral
-- Project Name: Schweigi NASM simulator - HW
-- Target Devices:
-- Tool Versions:
-- Description:
--
-- Dependencies:
--
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
----------------------------------------------------------------------------------
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.numeric_std.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

ENTITY top IS

  GENERIC (
    data_width : INTEGER := 8;
    data_length : INTEGER := 26;
    addr_width : INTEGER := 8;
    CLK_P_BITS : INTEGER := 5208; --50MHz -> 9600
    Half_Bit : INTEGER := 2604 -- half bit time
  );

  PORT (
    clk : INOUT STD_LOGIC; --system clock (def 12 MHz)
    upload : IN std_logic; --external source indicates RAM upload
    butt_clk : IN STD_LOGIC; -- clk driven by debounced push-button
    tx : OUT std_logic;
    rx_echo : OUT std_logic; --test output
    rx : in std_logic;
	 ser_clk_out : out std_logic
  );
END top;

ARCHITECTURE Behavioral OF top IS

component hs_uart
PORT (
    clk : IN std_logic;
    rx : IN std_logic;
    rx_echo : OUT std_logic;
    data_out : OUT std_logic_vector(7 DOWNTO 0);
    out_valid : OUT std_logic
  );
end component;


  COMPONENT bytetx
    PORT (
      clk : IN std_logic;
      inbyte : IN std_logic_vector(7 DOWNTO 0);
      l_clk : OUT std_logic;
      tx : OUT std_logic
    );
  END COMPONENT;
  
  
  COMPONENT ALU 
    Port ( argA : in STD_LOGIC_VECTOR (7 downto 0);
           argB : in STD_LOGIC_VECTOR (7 downto 0);
           res : inout STD_LOGIC_VECTOR (7 downto 0);
           sel : in STD_LOGIC_VECTOR (3 downto 0);
           Z : out std_logic;
           C : out std_logic);
  END COMPONENT;

  TYPE ram_type IS ARRAY (natural range <>) OF std_logic_vector (8 - 1 DOWNTO 0);
  subtype ram_stype is ram_type(0 to 26-1);
  subtype ram_mstype is ram_type(0 to 8+26-1);
  subtype ram_rstype is ram_type(0 to 3);

  
  --SIGNAL RAM : ram_stype := (OTHERS => (OTHERS => '0')); -- {x"1F", x"07", x"00", x"00", x"00", x"00", x"00", x"06", x"00", x"07", x"06", x"01", x"03", x"05", x"01", x"00", x"03", x"00", x"01", x"0A", x"00", x"01", x"1F", x"00", x"00"};
  --SIGNAL RAM : ram_stype := (x"1F", x"07", x"00", x"00", x"00", x"00", x"00", x"06", x"00", x"07", x"06", x"01", x"03", x"05", x"01", x"00", x"03", x"00", x"01", x"0A", x"02", x"01", x"1F", x"00", x"00");
  SIGNAL RAM : ram_stype := (x"38", x"07", x"00", x"00", x"00", x"00", x"00", x"06", x"00", x"07", x"06", x"01", x"03", x"05", x"01", x"00", x"32", x"00", x"36", x"01", x"0A", x"00", x"01", x"39", x"00", x"00");

  
  SIGNAL databus : std_logic_vector (8 - 1 DOWNTO 0);
  SIGNAL addr_reg : std_logic_vector (8 - 1 DOWNTO 0) := (OTHERS => '0');
  SIGNAL data_reg : std_logic_vector (8 - 1 DOWNTO 0);
  --TYPE reg_type IS ARRAY (0 TO 3) OF std_logic_vector (8 - 1 DOWNTO 0);
  SIGNAL A2D : ram_rstype := (OTHERS => (OTHERS => '0'));--registers A to D
  SIGNAL SP : std_logic_vector (8 - 1 DOWNTO 0) := std_logic_vector(to_unsigned(26-1, 8)); --stack pt set to last mem location
  SIGNAL IR,IP : std_logic_vector (8 - 1 DOWNTO 0) := (OTHERS => '0'); --instruction pointer
  SIGNAL H : std_logic_vector (8 - 1 DOWNTO 0) := (OTHERS => '0'); --Tannenbaum H reg (only for internal use)
  signal cpu_clk : std_logic := '0';

  SIGNAL Zf, Cf, Ff : std_logic; --flags
  SIGNAL RW : std_logic := '1';
  SIGNAL OE : std_logic := '0';
  TYPE state_type IS (fst1, fst2, fst3, wst1, wst2, wst3, wst4);
  SIGNAL state : state_type := fst1;
  TYPE I_state_type IS (ist1, ist2, ist3, ist4, ist5, ist6);
  SIGNAL I_state : I_state_type := ist1;
  SIGNAL cnt : INTEGER := 0;
  
  ------------------------------------------
  --signals for ALU
  signal argA, argB, res : STD_LOGIC_VECTOR (7 downto 0);
  signal ALUsel : STD_LOGIC_VECTOR (3 downto 0);
  signal Z,C : std_logic;
  
  
  --signals for testbus uart
  SIGNAL trbyte : std_logic_vector(7 DOWNTO 0);
  SIGNAL lclk : std_logic;
  SIGNAL t_clk : std_logic := '0';
  SIGNAL clk_div_cnt : INTEGER := 0;
  SIGNAL RAM_mirror : ram_mstype; -- := (x"23", x"00", x"30", x"06", x"01", x"0E", x"05", x"01", x"00", x"03", x"00", x"03", x"1F", x"00", x"24");-- (others => (others => '0'));
  SIGNAL SP_mirror, IR_mirror : std_logic_vector (8 - 1 DOWNTO 0); -- := (OTHERS => '0'); --stack pt and instruction reg
  SIGNAL IP_mirror : std_logic_vector (8 - 1 DOWNTO 0); -- := (OTHERS => '0'); --instruction pointer
  SIGNAL H_mirror : std_logic_vector (8 - 1 DOWNTO 0); -- := (OTHERS => '0'); --Tannenbaum H reg (only for internal use)
  signal tb_byte_cnt : integer := 0;
  TYPE esc_state_type IS (nulll,esc);
  signal esc_state : esc_state_type := nulll;

-- signals for program upload
  SIGNAL rxbyte : std_logic_vector(7 DOWNTO 0);
  signal rx_clk : std_logic;
  SIGNAL rxbyte_c : std_logic_vector(7 DOWNTO 0):= x"23"; --(OTHERS => '0'); --inclocked rxbyte
  signal rx_cnt : integer := 0;
  signal rx_state : esc_state_type  := nulll;

BEGIN

uart : hs_uart
  PORT MAP(
    clk => clk, 
    rx => rx,
    rx_echo => rx_echo,
    data_out => rxbyte, 
    out_valid => rx_clk
  );


  btx : bytetx
  PORT MAP(
    clk => t_clk, 
    inbyte => trbyte, 
    l_clk => lclk, 
    tx => tx
  );
  
  aluI : ALU 
    Port MAP ( 
           argA => argA,
           argB => argB,
           res => res,
           sel => ALUsel,
           Z => Z,
           C => C
   );

  --testbus mirroring
  RAM_mirror(8+0 TO 8+26 - 1) <= RAM(0 TO 26 - 1);
  RAM_mirror(0 TO 3) <= A2D;
  RAM_mirror(4) <= SP;
  RAM_mirror(5) <= IP;
  RAM_mirror(6) <= IR;
  RAM_mirror(7) <= "00000" & Zf & Cf & Ff;
  

  --RW determines who drives the databus
  databus <= data_reg WHEN OE = '0' ELSE
             RAM(to_integer(unsigned(addr_reg)));
             
 with IR select
      ALUsel <= "0000" when x"0A", --add
                "0001" when x"0E" , --sub
                "0010" when x"5A" , --shl
                "0011" when x"5E" , --shr
                "0100" when x"46" , --and
                "0101" when x"4A" , --or
                "0110" when x"4E" , --xor
                "0000" when others;
        
 cpu_clk <= butt_clk; --set clk to single stepping
 ser_clk_out <= clk; -- for testing serial baud rate

  cpu : PROCESS (cpu_clk)
  
PROCEDURE reset IS
  BEGIN
    A2D <= (OTHERS => (OTHERS => '0'));
    --SP <= (OTHERS => '0');
    SP <= std_logic_vector(to_unsigned(26-1, 8)); --stack pt set to last mem location

    IR <= (OTHERS => '0');
 
    IP <= (OTHERS => '0');
    H <= (OTHERS => '0');

    Zf <= '0';
    Cf <= '0';
    Ff <= '0';
    
    state <= fst1;
    I_state <= ist1;
--    esc_state <= nulll;
--    rx_state <= nulll;
    
END PROCEDURE reset;


    PROCEDURE opcode_fetch IS

    BEGIN
      CASE (state) IS
        WHEN fst1 => 
          OE <= '1';
          --IP <= "00000001"; --set instruction pointer
          addr_reg <= IP; --set memory adress to fetch opcode
          state <= fst2;
        WHEN fst2 => 
          IR <= databus; --read opcode into instruction register
          state <= fst3;
          OE <= '0';
          I_state <= ist1;
        WHEN OTHERS => 
      END CASE;
    END PROCEDURE opcode_fetch;

    PROCEDURE mem_write IS --addr_reg and data_reg are assumed set by instructon
      BEGIN
        CASE (state) IS
          WHEN wst1 => 
            RW <= '1';
            state <= wst2;
          WHEN wst2 => 
            OE <= '0';
            state <= wst3;
          WHEN wst3 => 
            RW <= '0'; -- write to mem in next clk cycle
            state <= wst4;
          WHEN wst4 => 
            RW <= '1';
            state <= fst1; -- back to opcode fetch
          WHEN OTHERS => 
        END CASE;
      END PROCEDURE mem_write;
 
 
 BEGIN
  IF (cpu_clk'EVENT AND cpu_clk = '1') THEN
    --IF (butt_clk'EVENT AND butt_clk = '1') THEN
    IF (upload = '1') THEN
      reset;
    ELSE

      CASE (state) IS
        WHEN fst1 | fst2 => 
          opcode_fetch;
        WHEN fst3 => 
          CASE (IR) IS
            WHEN x"1F" => --jmp
              CASE(I_state) IS
                WHEN ist1 => 
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --address is IP+1
                  I_state <= ist2;
                WHEN ist2 => 
                  OE <= '1'; --prepare for reading jmp adress
                  I_state <= ist3;
                WHEN ist3 => 
                  IP <= databus; -- read jmp adress into instruction pointer
                  OE <= '0';
                  state <= fst1;
                WHEN OTHERS => 
            END CASE; -- I_state for jmp
            
            WHEN x"06" => --move constant into register - register number is 1st arg
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1'; --prepare for reading
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --address is IP+1
                  I_state <= ist2;
                WHEN ist2 => 
                  data_reg <= databus; -- read register number
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --address is IP+2
                  I_state <= ist3;
                WHEN ist3 =>  
                  A2D(to_integer(unsigned(data_reg))) <= databus; --write constant from ram to register
                  OE <= '0';
                  IP <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 3, 8)); --IP forwarded by 3
                  state <= fst1;
                when others =>
              END CASE; --I_state - mov cnst to reg
              
            WHEN x"32" => --push register
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1'; --prepare for reading
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --register number
                  I_state <= ist2;
                WHEN ist2 => 
                  data_reg <= A2D(to_integer(unsigned(databus)));
                  addr_reg <= SP;
                  SP <= std_logic_vector(to_unsigned(to_integer(unsigned(SP))-1, 8)); -- decrement stack pointer
                  IP <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --IP forwarded by 3
                  state <= wst1;
                when others =>
              END CASE; --I_state - push reg to stack
              
            WHEN x"36" => --pop register
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1'; --prepare for reading
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --register number
                  I_state <= ist2;
                WHEN ist2 => 
                  data_reg <= databus;
                  --addr_reg <= SP;
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(SP))+1, 8));
                  SP <= std_logic_vector(to_unsigned(to_integer(unsigned(SP))+1, 8)); -- decrement stack pointer
                  IP <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --IP forwarded by 3
                  I_state <= ist3;
                WHEN ist3 => 
                  A2D(to_integer(unsigned(data_reg))) <= databus;
                  state <= fst1;
                when others =>
              END CASE; --I_state - pop reg from stack
            
            WHEN x"05" => -- write from register to mem adress
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1';
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --retrieve register no.
                  I_state <= ist2;
                WHEN ist2 => 
                  data_reg <= A2D(to_integer(unsigned(databus)));
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --retreive mem adress
                  I_state <= ist3;
                WHEN ist3 => 
                  addr_reg <= A2D(to_integer(unsigned(databus))); --mem-adress is in addr-reg
                  IP <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 3, 8)); --IP forwarded by 3
                  state <= wst1; --write to mem with data_reg and addr_reg set
                WHEN ist4 TO ist6 => 
            END CASE; --I_state for x05
            
            WHEN x"03" => -- write from register to mem adress
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1';
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --retrieve tx register no.
                  I_state <= ist2;
                WHEN ist2 => 
                  H <= databus; -- rx reg no stored in H A2D(to_integer(unsigned(databus))); --retrieve content from tx reg
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --retreive reg no for mem rx addr
                  I_state <= ist3;
                WHEN ist3 => 
                  addr_reg <= A2D(to_integer(unsigned(databus))); --mem-adress is in addr-reg
                  I_state <= ist4;
                WHEN ist4 => 
                  A2D(to_integer(unsigned(H))) <= databus;
                  IP <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 3, 8)); --IP forwarded by 3
                  state <= fst1;
                WHEN ist5 TO ist6 => 
            END CASE; --I_state for x39
            
            WHEN x"39" => -- return
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1';
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(SP))+1, 8)); --retrieve return adress
                  I_state <= ist2;
                WHEN ist2 => 
                  IP <= databus; -- set IP to return adress 
                  SP <= std_logic_vector(to_unsigned(to_integer(unsigned(SP))+1, 8)); -- increment stack pointer
                  I_state <= ist3;
                WHEN ist3 => 
                  state <= fst1; --back to instruction fetch
                WHEN ist4 TO ist6 => 
            END CASE; --I_state for x39 return
            
            WHEN x"38" => -- call
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1';
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --retrieve jmp adress
                  I_state <= ist2;
                WHEN ist2 => 
                  data_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --retreive return adress
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(SP)), 8)); --retrieve stack adress to store return adress
                  SP <= std_logic_vector(to_unsigned(to_integer(unsigned(SP))-1, 8)); -- decrement stack pointer
                  IP <= databus; -- read jmp adress
                  I_state <= ist3;
                WHEN ist3 => 
                  state <= wst1; --write to mem with data_reg and addr_reg set
                WHEN ist4 TO ist6 => 
            END CASE; --I_state for x38 call
   
            WHEN x"0A"|x"0E"|x"5A"|x"5E"|x"46"|x"4A"|x"4E" => --all implemented ALU ops, selection done through ALUsel above
              CASE(I_state) IS
                WHEN ist1 => 
                  OE <= '1';
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 1, 8)); --retrieve tx register no.
                  I_state <= ist2;
                WHEN ist2 => 
                  H <= databus; -- rx reg no stored in H A2D(to_integer(unsigned(databus))); --retrieve content from tx reg
                  addr_reg <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 2, 8)); --retreive reg no for mem rx addr
                  I_state <= ist3;
                WHEN ist3 =>  
                  --data_reg <= databus;
                  argA <= A2D(to_integer(unsigned(H)));
                  --argB <= A2D(to_integer(unsigned(data_reg)));
                  argB <= A2D(to_integer(unsigned(databus)));
                  --sel <= "0000"; --selector for add in ALU
                  I_state <= ist4;
                WHEN ist4 =>
                  A2D(to_integer(unsigned(H))) <= res; --write to register
                  Zf <= Z;
                  Cf <= C;
                  IP <= std_logic_vector(to_unsigned(to_integer(unsigned(IP)) + 3, 8)); --IP forwarded by 3
                  state <= fst1;
                WHEN ist5 to ist6 => 
              END CASE; --I_state for x0A add

            WHEN OTHERS => --OPcodes
              --;
        END CASE; --opcodes

        WHEN wst1 | wst2 | wst3 | wst4 => 
          mem_write;
      END CASE; --outer states
    END IF;
  END IF; --upload
END PROCESS;

      mem : PROCESS (clk)
      BEGIN
        --IF (clk'EVENT AND clk = '1' AND (RW = '0' or upload = '1')) THEN
        IF (clk'EVENT AND clk = '1') THEN
        
          if(RW = '0' and upload = '0') then
            RAM(to_integer(unsigned(addr_reg))) <= databus;
          end if;
          
          if(upload = '1' and rx_cnt>0) then --external programming of RAM
            RAM(rx_cnt-1) <= rxbyte_c;
          end if;
          
        end if;
      END PROCESS;
      
      --clock divider from 50MHz to 9600 baud
      PROCESS (clk)
        BEGIN
          IF (clk'EVENT AND clk = '1') THEN
            IF (clk_div_cnt < 2604) THEN
              clk_div_cnt <= clk_div_cnt + 1;
            ELSE
              clk_div_cnt <= 0;
              t_clk <= NOT t_clk;
            END IF;
          END IF;
        END PROCESS;
        
      PROCESS (lclk)
        BEGIN
          IF (lclk'EVENT AND lclk = '1') THEN
            if(tb_byte_cnt = 0) then
               trbyte <= x"24"; --$ for frame start delimiter
               tb_byte_cnt <= tb_byte_cnt + 1;
               esc_state <= nulll;
            else
              if (tb_byte_cnt = 8+26+1) then
                trbyte <= x"23"; --# for frame end delimiter
                tb_byte_cnt <= 0;
              else
                if(esc_state = nulll) then 
                   if(RAM_mirror(tb_byte_cnt-1) = x"23" or RAM_mirror(tb_byte_cnt-1) = x"24" or RAM_mirror(tb_byte_cnt-1) = x"2F") then --escaped char
                     trbyte <= x"2F"; --send esc char
                     esc_state <= esc;
                   else --no esc-char
                     trbyte <= RAM_mirror(tb_byte_cnt-1);
                     tb_byte_cnt <= tb_byte_cnt + 1;
                   end if; --esc-char
                 else  --esc state
                   trbyte <= RAM_mirror(tb_byte_cnt-1) xor x"03";
                   tb_byte_cnt <= tb_byte_cnt + 1;
                   esc_state <= nulll;
                 end if; --esc-state
               end if; --length
             end if; -- =0
          END IF; --clk
        END PROCESS;
        
        
process (rx_clk) --receive byte from uart
begin
   if (rx_clk'event and rx_clk = '1') then
     if(rxbyte = x"24") then --start delimiter $
        rx_cnt <= 0;
        rx_state <= nulll;
     else
       if(rx_state = esc) then
         rxbyte_c <= rxbyte xor x"03";
         rx_cnt <= rx_cnt + 1;
         rx_state <= nulll;
       else
         if(rxbyte = x"2F") then --esc char /
           rx_state <= esc;
         else
           rxbyte_c <= rxbyte;
           rx_cnt <= rx_cnt + 1;
         end if;
       end if;
     end if;
     
   end if;
end process;

END Behavioral;