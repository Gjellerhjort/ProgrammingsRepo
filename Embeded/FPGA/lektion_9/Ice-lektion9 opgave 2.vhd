-- Quartus Prime VHDL Template
-- Basic Shift Register

library ieee;
use ieee.std_logic_1164.all;

entity lektion9 is


	port 
	(
		a		: in std_logic_vector(3 downto 0);
		b		: out std_logic_vector(3 downto 0);
		rd		: in std_logic;
		wr		: in std_logic
		
	);

end entity;

architecture rtl of lektion9 is
		
		
		


begin

	process ()
	
	variable memory std_logic_vector(3 downto 0);
	begin
	
	if (wr) then
	
	memory := a	
	
	end if;
	if (rd) then
	
	b <= memory
	
	end if;

	
	
	end process;

end rtl;
