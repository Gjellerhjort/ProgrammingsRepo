library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity MemoryBlockArray is
    port (
        a     : in std_logic_vector(3 downto 0);  -- Data input
        b     : out std_logic_vector(3 downto 0); -- Data output
        addr  : in std_logic_vector(1 downto 0);  -- 2-bit address input for 4 locations
        rd    : in std_logic;                     -- Read enable
        wr    : in std_logic                      -- Write enable
    );
end entity;

architecture rtl of MemoryBlockArray is
    type memory_array_type is array (0 to 3) of std_logic_vector(3 downto 0); -- 4x4-bit memory array
    signal memory : memory_array_type;         -- Initialize to 0
begin

    process (wr, rd)
    begin
        if wr = '0' then
            memory(to_integer(unsigned(addr))) <= a; -- Write to selected address
        end if;

        if rd = '0' then
            b <= memory(to_integer(unsigned(addr))); -- Read from selected address
        else
            b <= (others => 'Z');                   -- High-impedance when not reading
        end if;
    end process;

end rtl;
