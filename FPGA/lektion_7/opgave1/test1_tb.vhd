library ieee;
use ieee.std_logic_1164.all;

entity test1_tb is
end entity;

architecture sim of test1_tb is
    -- Component Declaration for test1
    component test1
        port(
            switch0 : in std_logic;
            switch1 : in std_logic;
            switch2 : in std_logic;
            switch3 : in std_logic;
            led0    : out std_logic;
            led1    : out std_logic;
            led2    : out std_logic;
            led3    : out std_logic
        );
    end component;

    -- Signals for connecting to the DUT
    signal switch0, switch1, switch2, switch3 : std_logic := '0';
    signal led0, led1, led2, led3 : std_logic;

begin
    -- Instantiate the Design Under Test (DUT)
    DUT: test1
        port map (
            switch0 => switch0,
            switch1 => switch1,
            switch2 => switch2,
            switch3 => switch3,
            led0    => led0,
            led1    => led1,
            led2    => led2,
            led3    => led3
        );

    -- Stimulus Process
    stim_proc: process
    begin
        -- Test Case 1
        switch0 <= '1'; switch1 <= '0'; switch2 <= '1'; switch3 <= '0';
        wait for 10 ns;

        -- Test Case 2
        switch0 <= '0'; switch1 <= '1'; switch2 <= '0'; switch3 <= '1';
        wait for 10 ns;

        -- Test Case 3
        switch0 <= '1'; switch1 <= '1'; switch2 <= '0'; switch3 <= '0';
        wait for 10 ns;

        -- Finish Simulation
        wait;
    end process;

end architecture;
