-- 1-bit Full Adder in VHDL

library ieee;
use ieee.std_logic_1164.all;

entity adder4 is
	
	port
	(
		-- ports
		A	: in  STD_LOGIC_VECTOR(3 downto 0);
		B	: in  STD_LOGIC_VECTOR(3 downto 0);
		S 	: out STD_LOGIC_VECTOR(4 downto 0)
	);
end adder4;


architecture ark of adder4 is

	signal C:  STD_LOGIC_VECTOR(2 downto 0);


component adder

	port
	(
		A     : in std_logic;  -- First input bit
		B     : in std_logic;  -- Second input bit
		Cin   : in std_logic;  -- Carry input
		S     : out std_logic; -- Sum output
		Cout  : out std_logic  -- Carry output
		
	);
end component;

begin

   a1 : adder port map 
	(
		A	 => A(0),  -- First input bit
		B	 => B(0),   -- Second input bit
		Cin => '0',  -- Carry input
		S	 => S(0),   -- Sum output
		Cout => C(0)    -- Carry output
	);
	
	a2 : adder port map 
	(
		A	 => A(1),  	-- First input bit
		B	 => B(1),   -- Second input bit
		Cin => C(0),  		-- Carry input
		S	 => S(1),   -- Sum output
		Cout => C(1)    	-- Carry output
	);

   a3 : adder port map 
	(
		A	 => A(2),  -- First input bit
		B	 => B(2),   -- Second input bit
		Cin => C(1),  -- Carry input
		S	 => S(2),   -- Sum output
		Cout => C(2)    -- Carry output
	);
	
	a4 : adder port map 
	(
		A	 => A(3),  	-- First input bit
		B	 => B(3),   -- Second input bit
		Cin => C(2),  		-- Carry input
		S	 => S(3),   -- Sum output
		Cout => S(4)    	-- Carry output
	);
	
  

end ark;
