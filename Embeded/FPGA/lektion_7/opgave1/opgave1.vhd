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
		led0	: out std_logic;
		led1	: out std_logic;
		led2	: out std_logic;
		led3	: out std_logic
	);

end entity;

architecture rtl of test1 is



begin
	led0 <= switch0;
	led1 <= switch1;
	led2 <= switch2;
	led3 <= switch3;

end rtl;
