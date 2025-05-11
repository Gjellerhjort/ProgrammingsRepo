-- Quartus Prime VHDL Template
-- Basic Shift Register

library ieee;
use ieee.std_logic_1164.all;

entity shiftRegister1 is

	port 
	(
		btn	: in std_logic; -- Button input
		swtch : in std_logic; -- Switch input
		LED	: out std_logic_vector(3 downto 0) -- LED output
	);

end entity;

architecture rtl of shiftRegister1 is
    signal buff: std_logic_vector(3 downto 0) := (others => '0'); -- Initialize buff to all 0s
begin

    process (btn)
    begin
        if falling_edge(btn) then
            buff(3) <= buff(2);
            buff(2) <= buff(1); 
            buff(1) <= buff(0);
            buff(0) <= swtch;

            LED <= buff; -- Directly assign buff to LED
        end if;
    end process;

end rtl;
