library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity icelection9_tb is
-- Testbench has no ports
end entity;

architecture testbench of icelection9_tb is
    -- Component declaration for the Unit Under Test (UUT)
    component icelection9
        port (
            clk  : in std_logic;
            leds : out std_logic_vector(5 downto 0)
        );
    end component;

    -- Signals for the UUT
    signal clk  : std_logic := '0';
    signal leds : std_logic_vector(5 downto 0);

    -- Clock period
    constant clk_period : time := 10 ns;

begin
    -- Instantiate the Unit Under Test (UUT)
    uut: icelection9
        port map (
            clk  => clk,
            leds => leds
        );

    -- Clock generation process
    clock_gen: process
    begin
        while true loop
            clk <= '0';
            wait for clk_period / 2;
            clk <= '1';
            wait for clk_period / 2;
        end loop;
    end process;

    -- Stimulus process
    stimulus: process
    begin
        -- Wait for a few clock cycles to observe the behavior
        wait for 600 ns;

        -- Finish the simulation
        wait;
    end process;

end architecture;
