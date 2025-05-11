library ieee;
use ieee.std_logic_1164.all;

entity MemoryBlock4_tb is
end entity;

architecture sim of MemoryBlock4_tb is
    -- Component Declaration for MemoryBlock4
    component MemoryBlock4
        port (
            a     : in std_logic_vector(3 downto 0);
            b     : out std_logic_vector(3 downto 0);
            rd    : in std_logic;
            wr    : in std_logic
        );
    end component;

    -- Signals for connecting to the DUT
    signal a   : std_logic_vector(3 downto 0); -- Input memory
    signal b   : std_logic_vector(3 downto 0); -- Output memory
    signal rd  : std_logic := '1'; -- Read enable, initially disabled
    signal wr  : std_logic := '1'; -- Write enable, initially disabled

begin
    -- Instantiate the Design Under Test (DUT)
    DUT: MemoryBlock4
        port map (
            a  => a,
            b  => b,
            rd => rd,
            wr => wr
        );

    -- Stimulus Process
    stim_proc: process
    begin
        -- Test Case 1: Write value to memory
        a <= "1010";    -- Input data
        wr <= '0';      -- Enable write
        wait for 10 ns;
        wr <= '1';      -- Disable write
        wait for 10 ns;

        -- Test Case 2: Read value from memory
        rd <= '0';      -- Enable read
        wait for 10 ns;
        rd <= '1';      -- Disable read
        wait for 10 ns;

        -- Test Case 3: Overwrite memory with new value
        a <= "1100";    -- New input data
        wr <= '0';      -- Enable write
        wait for 10 ns;
        wr <= '1';      -- Disable write
        wait for 10 ns;

        -- Test Case 4: Read updated value from memory
        rd <= '0';      -- Enable read
        wait for 10 ns;
        rd <= '1';      -- Disable read
        wait for 10 ns;

        -- Test Case 5: Check high-impedance behavior when not reading
        -- Finish Simulation
        wait;
    end process;

end architecture;
