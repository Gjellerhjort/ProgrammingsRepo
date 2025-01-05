-- Quartus Prime VHDL Template
-- Basic Shift Register without Clock

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity icelection9 is
    port (
        clk      : in std_logic;              -- Add clock input
        leds     : out std_logic_vector(5 downto 0)
    );
end entity;

architecture rtl of icelection9 is
begin

    process (clk)
        variable count : integer := 0;
    begin
        if rising_edge(clk) then                   -- Edge detection for clock
            if (count >= 59) then
					count := 0;
				else
					count := count + 1;
				end if;
            leds <= std_logic_vector(to_unsigned(count, leds'length));
        end if;
    end process;

end rtl;
