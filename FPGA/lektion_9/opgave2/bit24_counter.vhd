-- Quartus Prime VHDL Template
-- Basic Shift Register

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity bit24_counter is

	port 
	(
		clk	: in std_logic; -- clk input
		number	: out std_logic_vector(23 downto 0) -- LED output
	);

end entity;

architecture rtl of bit24_counter is
begin
    process (clk)
        variable count : integer := 0;
    begin
        if rising_edge(clk) then                   -- Edge detection for clock
            if (count > 16777215) then
					count := 0;
				else
					count := count + 1;
				end if;
            number <= std_logic_vector(to_unsigned(count, 24));
        end if;
    end process;
end rtl;
