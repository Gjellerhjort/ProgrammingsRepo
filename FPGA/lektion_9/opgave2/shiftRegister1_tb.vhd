library ieee;
use ieee.std_logic_1164.all;

entity shiftRegister1_tb is
end entity;

architecture sim of shiftRegister1_tb is
    -- Component Declaration for shiftRegister1
    component shiftRegister1
        port (
            btn   : in std_logic;
            swtch : in std_logic;
            LED   : out std_logic_vector(3 downto 0)
        );
    end component;

    -- Signals to connect to the DUT
    signal btn   : std_logic := '1'; -- Button input, initially inactive
    signal swtch : std_logic := '0'; -- Switch input
    signal LED   : std_logic_vector(3 downto 0); -- LED output

begin
    -- Instantiate the Design Under Test (DUT)
    DUT: shiftRegister1
        port map (
            btn   => btn,
            swtch => swtch,
            LED   => LED
        );

    -- Stimulus Process
    stim_proc: process
    begin
        -- Test Case 1: Shift in '1'
        -- expected LED output: 0001
        swtch <= '1';          -- Switch set to '1'
        btn <= '0';            -- Button pressed
        wait for 10 ns;
        btn <= '1';            -- Button released
        wait for 10 ns;

        -- Test Case 2: Shift in '0'
        -- expected LED output: 0010
        swtch <= '0';          -- Switch set to '0'
        btn <= '0';            -- Button pressed
        wait for 10 ns;
        btn <= '1';            -- Button released
        wait for 10 ns;

        -- Test Case 3: Shift in '1'
        -- expected LED output: 0101
        swtch <= '1';          -- Switch set to '1'
        btn <= '0';            -- Button pressed
        wait for 10 ns;
        btn <= '1';            -- Button released
        wait for 10 ns;

        -- Test Case 4: Verify full shift register operation
        -- expected LED output: 1010
        swtch <= '0';          -- Switch set to '0'
        btn <= '0';            -- Button pressed
        wait for 10 ns;
        btn <= '1';            -- Button released
        wait for 10 ns;

        -- Test Case 5: Verify full shift register operation
        -- expected LED output: 0101
        swtch <= '1';          -- Switch set to '1'
        btn <= '0';            -- Button pressed
        wait for 10 ns;
        btn <= '1';            -- Button released
        wait for 10 ns;

        -- Finish simulation
        wait;
    end process;

end architecture;
