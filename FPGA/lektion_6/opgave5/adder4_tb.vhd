library ieee;
use ieee.std_logic_1164.all;

entity adder4_tb is
end entity;

architecture sim of adder4_tb is
    -- Component Declaration for adder4
    component adder4
        port (
            A  : in  std_logic_vector(3 downto 0); -- 4-bit input A
            B  : in  std_logic_vector(3 downto 0); -- 4-bit input B
            S  : out std_logic_vector(4 downto 0)  -- 5-bit output sum
        );
    end component;

    -- Signals for connecting to the DUT
    signal A, B : std_logic_vector(3 downto 0) := (others => '0');
    signal S    : std_logic_vector(4 downto 0);

begin
    -- Instantiate the Design Under Test (DUT)
    DUT: adder4
        port map (
            A => A,
            B => B,
            S => S
        );

    -- Stimulus Process
    stim_proc: process
    begin
        -- Test Case 1: Add 3 + 5
        A <= "0011"; -- 3 in binary
        B <= "0101"; -- 5 in binary
        wait for 20 ns;

        -- Test Case 2: Add 7 + 8
        A <= "0111"; -- 7 in binary
        B <= "1000"; -- 8 in binary
        wait for 20 ns;

        -- Test Case 3: Add 15 + 1
        A <= "1111"; -- 15 in binary
        B <= "0001"; -- 1 in binary
        wait for 20 ns;

        -- Test Case 4: Add 0 + 0
        A <= "0000"; -- 0 in binary
        B <= "0000"; -- 0 in binary
        wait for 20 ns;

        -- Test Case 5: Add 10 + 13
        A <= "1010"; -- 10 in binary
        B <= "1101"; -- 13 in binary
        wait for 20 ns;

        -- Finish simulation
        wait;
    end process;

end architecture;
