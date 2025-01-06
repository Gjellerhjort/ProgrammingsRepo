-----------------------------------------------------------
-- uart_rx.vhd
-----------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.std_logic_unsigned.ALL;
USE ieee.numeric_std.ALL;
USE IEEE.std_logic_arith.ALL;
ENTITY hs_uart IS
  GENERIC (
    CLK_P_BITS : INTEGER := 1250; --12MHz -> 9600
    Half_Bit : INTEGER := 625 -- half bit time
  );
  PORT (
    clk : IN std_logic;
    rx : IN std_logic;
    rx_echo : OUT std_logic;
    data_out : OUT std_logic_vector(7 DOWNTO 0);
    out_valid : OUT std_logic
  );
END ENTITY hs_uart;

ARCHITECTURE behavioural OF hs_uart IS
  TYPE rx_state IS (idle, start_bit, receive_data,stop_bit);
  SIGNAL current_state : rx_state := idle;
  SIGNAL data_counter : INTEGER := 0; -- no of bits received
  SIGNAL counter : INTEGER; --divides clks to bits
  SIGNAL data_buffer : std_logic_vector(7 DOWNTO 0) := (OTHERS => '0');
  SIGNAL data_next : std_logic_vector(7 DOWNTO 0) := (OTHERS => '0');
  SIGNAL data_valid : std_logic := '0';
  SIGNAL startbit : std_logic := '0';
  --SIGNAL wait_cnt : integer := 0;
  SIGNAL r_RX_Data_R : std_logic;
  SIGNAL r_RX_Data : std_logic;
  
BEGIN
  data_next(6 DOWNTO 0) <= data_buffer(7 DOWNTO 1);
  data_next(7) <= r_RX_Data; -- receive 1st data bit

--  data_next(7 DOWNTO 1) <= data_buffer(6 DOWNTO 0);
--  data_next(0) <= r_RX_Data; -- receive 1st data bit
  rx_echo <= data_next(7);
  
  out_valid <= data_valid;


  p_SAMPLE : PROCESS (clk) --to prevent meta-stability
  BEGIN
    IF rising_edge(clk) THEN
      r_RX_Data_R <= rx;
      r_RX_Data <= r_RX_Data_R;
    END IF;
  END PROCESS p_SAMPLE;

  rx_proc : PROCESS (clk)
  BEGIN
    IF (clk = '1' AND clk'event) THEN
      IF (current_state = idle AND r_RX_Data = '0') THEN
        current_state <= start_bit;
        counter <= Half_Bit; -- waiting until middle of first bit
        data_counter <= 0; -- no data received yet
      END IF;
      IF (current_state = start_bit) THEN
        IF (counter > 0) THEN
          counter <= counter - 1;
        ELSE
          data_buffer <= data_next; --FSM clocking of FF
          current_state <= receive_data;
          data_counter <= data_counter + 1;
          counter <= CLK_P_BITS;
          data_valid <= '0'; -- prepare for later positive edge
        END IF;
      END IF;
      IF (current_state = receive_data) THEN
        IF (counter > 0) THEN
          counter <= counter - 1;
        ELSE
          IF (data_counter < 9) THEN
            data_buffer <= data_next;
            counter <= CLK_P_BITS; -- wait until middle of next bit
            data_counter <= data_counter + 1;
            IF (data_counter = 8) THEN -- last bit received
              data_out <= data_next; --clocking data out - valid until next byte
            END IF;
          ELSE --stop bit
            current_state <= stop_bit; -- wait for next start bit
            counter <= CLK_P_BITS; -- wait until middle of next bit
          END IF;
        END IF;
      END IF;
      
      IF (current_state = stop_bit) THEN
        IF (counter > 0) THEN
          counter <= counter - 1;
        ELSE
           current_state <= idle; -- wait for next start bit
           --data_valid <= NOT data_valid; -- toggle to indicate new data byte
           data_valid <= '1'; -- positive edge for receiving side
        END IF;
      END IF;
        
    END IF;
END PROCESS rx_proc;
END behavioural;