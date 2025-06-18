library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity MemoryBlockArray_tb is
end entity;

architecture testbench of MemoryBlockArray_tb is
    -- Component declaration
    component MemoryBlockArray
        port (
            a     : in std_logic_vector(3 downto 0);
            b     : out std_logic_vector(3 downto 0);
            addr  : in std_logic_vector(1 downto 0);
            rd    : in std_logic;
            wr    : in std_logic
        );
    end component;

    -- Testbench signals
    signal a     : std_logic_vector(3 downto 0);
    signal b     : std_logic_vector(3 downto 0); -- Fully constrained
    signal addr  : std_logic_vector(1 downto 0);
    signal rd    : std_logic := '1'; -- Default inactive
    signal wr    : std_logic := '1'; -- Default inactive

    -- Signal to hold the memory log
    type memory_array is array (0 to 3) of std_logic_vector(3 downto 0);
    signal memory : memory_array := (others => (others => '0'));  -- Initialize all memory to 0
    -- Clock simulation (if needed)
    constant clk_period : time := 10 ns;

begin
    -- Instantiate the memory block array
    uut: MemoryBlockArray
        port map (
            a => a,
            b => b,
            addr => addr,
            rd => rd,
            wr => wr
        );

    -- Test process
    process
    begin
        -- Test 1: Write to all memory locations
        for i in 0 to 3 loop
            addr <= std_logic_vector(to_unsigned(i, 2)); -- Select memory address
            a <= std_logic_vector(to_unsigned(i * 3, 4)); -- Write unique data
            wr <= '0'; -- Enable write
            wait for clk_period;
            wr <= '1'; -- Disable write
            wait for clk_period;
            memory(to_integer(unsigned(addr))) <= a;  -- Store the written value in the memory array
        end loop;

        -- Test 2: Read from all memory locations
        for i in 0 to 3 loop
            addr <= std_logic_vector(to_unsigned(i, 2)); -- Select memory address
            rd <= '0'; -- Enable read
            wait for clk_period;
            assert b = std_logic_vector(to_unsigned(i * 3, 4))
                report "Read mismatch at address " & integer'image(i)
                severity error;
            rd <= '1'; -- Disable read
            wait for clk_period;
        end loop;

        -- Test 3: Check high-impedance output when not reading
        rd <= '1'; -- Disable read
        wait for clk_period;
        assert b = "ZZZZ" -- Check for high-impedance state
            report "Output not high-impedance when not reading"
            severity error;

        -- Finish simulation
        wait;
    end process;
end architecture;
