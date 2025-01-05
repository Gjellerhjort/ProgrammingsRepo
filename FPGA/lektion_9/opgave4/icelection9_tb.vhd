library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;  -- Include the numeric_std package

entity icelection9_tb is
-- Testbench has no ports
end icelection9_tb;

architecture Behavioral of icelection9_tb is
    -- Component declaration for the Unit Under Test (UUT)
    component icelection9
        Port (
            binary_in : in  STD_LOGIC_VECTOR (3 downto 0);
            segments  : out STD_LOGIC_VECTOR (6 downto 0)
        );
    end component;

    -- Signals to connect to the UUT
    signal binary_in : STD_LOGIC_VECTOR (3 downto 0) := "0000";
    signal segments  : STD_LOGIC_VECTOR (6 downto 0);

begin
    -- Instantiate the Unit Under Test (UUT)
    uut: icelection9
        Port map (
            binary_in => binary_in,
            segments  => segments
        );

    -- Stimulus process
    process
    begin
        -- Apply all possible values of binary_in
        for i in 0 to 15 loop
            binary_in <= std_logic_vector(to_unsigned(i, 4));
            wait for 10 ns;  -- Wait for output to stabilize
        end loop;

        -- Finish the simulation
        wait;
    end process;

end Behavioral;
