LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY top_w_proc_2_tb IS
END top_w_proc_2_tb;

ARCHITECTURE Behavioral OF top_w_proc_2_tb IS

  -- Component Declaration for the Unit Under Test (UUT)
  COMPONENT top
    GENERIC (
      data_width : INTEGER := 8;
      data_length : INTEGER := 26;
      addr_width : INTEGER := 8;
      CLK_P_BITS : INTEGER := 5208; -- 50MHz -> 9600
      Half_Bit : INTEGER := 2604 -- half bit time
    );
    PORT (
      clk         : INOUT STD_LOGIC; -- system clock (def 12 MHz)
      upload      : IN STD_LOGIC;   -- external source indicates RAM upload
      butt_clk    : IN STD_LOGIC;   -- clk driven by debounced push-button
      tx          : OUT STD_LOGIC;
      rx_echo     : OUT STD_LOGIC; -- test output
      rx          : IN STD_LOGIC;
      ser_clk_out : OUT STD_LOGIC
    );
  END COMPONENT;

  -- Signals for interfacing with the UUT
  SIGNAL clk         : STD_LOGIC := '0';
  SIGNAL upload      : STD_LOGIC := '0';
  SIGNAL butt_clk    : STD_LOGIC := '0';
  SIGNAL tx          : STD_LOGIC;
  SIGNAL rx_echo     : STD_LOGIC;
  SIGNAL rx          : STD_LOGIC := '0';
  SIGNAL ser_clk_out : STD_LOGIC;

  -- Clock generation parameters
  CONSTANT CLK_PERIOD : TIME := 20 ns; -- 50 MHz clock
  
BEGIN

  -- Instantiate the Unit Under Test (UUT)
  uut: top
    GENERIC MAP (
      data_width => 8,
      data_length => 26,
      addr_width => 8,
      CLK_P_BITS => 5208,
      Half_Bit => 2604
    )
    PORT MAP (
      clk => clk,
      upload => upload,
      butt_clk => butt_clk,
      tx => tx,
      rx_echo => rx_echo,
      rx => rx,
      ser_clk_out => ser_clk_out
    );

  -- Clock process for generating clk signal
  clk_process: PROCESS
  BEGIN
    clk <= '0';
    WAIT FOR CLK_PERIOD / 2;
    clk <= '1';
    WAIT FOR CLK_PERIOD / 2;
  END PROCESS;

  -- Stimulus process
  stimulus: PROCESS
  BEGIN
    -- Initialize Inputs
    upload <= '0';
    butt_clk <= '0';
    rx <= '0';

    -- Wait for global reset
    WAIT FOR 100 ns;

    -- Simulate RAM upload signal
    upload <= '1';
    WAIT FOR 40 ns;
    upload <= '0';

    -- Simulate button clock signal
    butt_clk <= '1';
    WAIT FOR 40 ns;
    butt_clk <= '0';

    -- Simulate RX signal
    rx <= '1';
    WAIT FOR 100 ns;
    rx <= '0';

    -- End simulation after sufficient time
    WAIT FOR 500 ns;
    ASSERT FALSE REPORT "End of simulation" SEVERITY NOTE;
    WAIT;
  END PROCESS;

END Behavioral;
