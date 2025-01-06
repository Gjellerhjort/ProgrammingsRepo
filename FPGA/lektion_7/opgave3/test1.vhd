-- Quartus Prime VHDL Template
-- Basic Shift Register

library ieee;
use ieee.std_logic_1164.all;

entity test1 is

	port 
	(
		switch0 : in std_logic;
		switch1 : in std_logic;
		switch2 : in std_logic;
		switch3 : in std_logic;
		led0	: out std_logic

	);

end entity;

architecture rtl of test1 is



begin
	led0 <= (switch0 AND switch1) OR NOT (switch2 AND switch3);
	
end rtl;
