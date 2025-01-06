-- 1-bit Full Adder in VHDL

library ieee;
use ieee.std_logic_1164.all;

entity test1 is
	port (
		A     : in std_logic;  -- First input bit
		B     : in std_logic;  -- Second input bit
		Cin   : in std_logic;  -- Carry input
		S     : out std_logic; -- Sum output
		Cout  : out std_logic  -- Carry output
	);
end entity;

architecture rtl of test1 is
begin
	-- Sum is A XOR B XOR Cin
	S <= A XOR B XOR Cin;
	
	-- Carry out is (A AND B) OR (Cin AND (A XOR B))
	Cout <= (A AND B) OR (Cin AND (A XOR B));
end rtl;

