-- Quartus Prime VHDL Template
-- Basic Shift Register without Clock

library ieee;
use ieee.std_logic_1164.all;

entity MemoryBlock4 is
    port (
        a     : in std_logic_vector(3 downto 0); -- Switch memory input
        b     : out std_logic_vector(3 downto 0); -- LED memory output
        rd    : in std_logic; -- BT0 is readEnable
        wr    : in std_logic -- BT1 is writeEnable
    );
end entity;

architecture rtl of MemoryBlock4 is
    signal memory : std_logic_vector(3 downto 0);
begin

    process (wr, rd)
    begin
        if wr = '0' then
            memory <= a;
        end if;
        
        if rd = '0' then
            b <= memory;
        else
            b <= (others => 'Z');  -- High-impedance when not reading
        end if;
    end process;

end rtl;
