library ieee;
use ieee.std_logic_1164.all;

entity test1_tb is
end entity;

architecture sim of test1_tb is
    -- Component Declaration for test1
    component test1
        port (
            switch0 : in std_logic;
            switch1 : in std_logic;
            led0    : out std_logic;
            led1    : out std_logic;
            led2    : out std_logic
        );
    end component;

    -- Signals for connecting to the DUT
    signal switch0, switch1 : std_logic := '0';
    signal led0, led1, led2 : std_logic;

begin
    -- Instantiate the Design Under Test (DUT)
    DUT: test1
        port map (
            switch0 => switch0,
            switch1 => switch1,
            led0    => led0,
            led1    => led1,
            led2    => led2
        );

    -- Stimulus Process
    stim_proc: process
    begin
        -- Test Case 1: switch0 = 0, switch1 = 0
        -- Expected: led0 = 0 AND 0 = 0, led1 = 0 OR 0 = 0, led2 = 0 XOR 0 = 0
        switch0 <= '0'; switch1 <= '0';
        wait for 10 ns;

        -- Test Case 2: switch0 = 0, switch1 = 1
        -- Expected: led0 = 0, led1 = 1, led2 = 1
        switch0 <= '0'; switch1 <= '1';
        wait for 10 ns;

        -- Test Case 3: switch0 = 1, switch1 = 0
        -- Expected: led0 = 1 AND 0 = 0, led1 = 1 OR 0 = 1, led2 = 1 XOR 0 = 1
        switch0 <= '1'; switch1 <= '0';
        wait for 10 ns;

        -- Test Case 4: switch0 = 1, switch1 = 1
        -- Expected: led0 = 1 AND 1 = 1, led1 = 1 OR 1 = 1, led2 = 1 XOR 1 = 0
        switch0 <= '1'; switch1 <= '1';
        wait for 10 ns;

        -- Finish Simulation
        wait;
    end process;

end architecture;
