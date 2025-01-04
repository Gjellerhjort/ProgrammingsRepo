library ieee;
use ieee.std_logic_1164.all;

entity test1_tb is
end entity;

architecture sim of test1_tb is
    -- Component Declaration for test1 (1-bit full adder)
    component test1
        port (
            A     : in std_logic;
            B     : in std_logic;
            Cin   : in std_logic;
            S     : out std_logic;
            Cout  : out std_logic
        );
    end component;

    -- Signals for connecting to the DUT (Design Under Test)
    signal A, B, Cin : std_logic := '0';
    signal S, Cout    : std_logic;

begin
    -- Instantiate the Design Under Test (DUT)
    DUT: test1
        port map (
            A     => A,
            B     => B,
            Cin   => Cin,
            S     => S,
            Cout  => Cout
        );

    -- Stimulus Process: This process applies different combinations of inputs
    stim_proc: process
    begin
        -- Test Case 1: A = 0, B = 0, Cin = 0 (Expected: S = 0, Cout = 0)
        A <= '0'; B <= '0'; Cin <= '0';
        wait for 10 ns;

        -- Test Case 2: A = 0, B = 0, Cin = 1 (Expected: S = 1, Cout = 0)
        A <= '0'; B <= '0'; Cin <= '1';
        wait for 10 ns;

        -- Test Case 3: A = 0, B = 1, Cin = 0 (Expected: S = 1, Cout = 0)
        A <= '0'; B <= '1'; Cin <= '0';
        wait for 10 ns;

        -- Test Case 4: A = 0, B = 1, Cin = 1 (Expected: S = 0, Cout = 1)
        A <= '0'; B <= '1'; Cin <= '1';
        wait for 10 ns;

        -- Test Case 5: A = 1, B = 0, Cin = 0 (Expected: S = 1, Cout = 0)
        A <= '1'; B <= '0'; Cin <= '0';
        wait for 10 ns;

        -- Test Case 6: A = 1, B = 0, Cin = 1 (Expected: S = 0, Cout = 1)
        A <= '1'; B <= '0'; Cin <= '1';
        wait for 10 ns;

        -- Test Case 7: A = 1, B = 1, Cin = 0 (Expected: S = 0, Cout = 1)
        A <= '1'; B <= '1'; Cin <= '0';
        wait for 10 ns;

        -- Test Case 8: A = 1, B = 1, Cin = 1 (Expected: S = 1, Cout = 1)
        A <= '1'; B <= '1'; Cin <= '1';
        wait for 10 ns;

        -- Finish simulation
        wait;
    end process;

end architecture;
