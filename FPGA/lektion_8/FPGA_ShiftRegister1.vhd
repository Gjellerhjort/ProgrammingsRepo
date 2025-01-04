-- Quartus Prime VHDL Template
-- Basic Shift Register

library ieee;
use ieee.std_logic_1164.all;

entity FPGA_ShiftRegister1 is

	port 
	(
		btn		: in std_logic;
		swtch	    : in std_logic;
		LED	: out std_logic_vector(3 downto 0)
	);

end entity;

architecture rtl of FPGA_ShiftRegister1 is
begin

	process (btn)
	variable buff: std_logic_vector(3 downto 0);
	begin
		if (btn = '0') then
			buff(3) := buff(2);
			buff(2) := buff(1);
			buff(1) := buff(0);
			buff(0) := swtch;
			
			LED(3) <= buff(3);
			LED(2) <= buff(2);
			LED(1) <= buff(1);
			LED(0) <= buff(0);
		end if;
	end process;
end rtl;
