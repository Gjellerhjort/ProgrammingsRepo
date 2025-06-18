library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity icelection9 is
    Port (
        binary_in : in  STD_LOGIC_VECTOR (3 downto 0);  -- 4-bit binary input
        segments  : out STD_LOGIC_VECTOR (6 downto 0)   -- 7-bit output for segments a-g
    );
end icelection9;

architecture Behavioral of icelection9 is
begin
    process(binary_in)
    begin
        case binary_in is
            when "0000" => segments <= "1000000"; -- 0
            when "0001" => segments <= "1111001"; -- 1
            when "0010" => segments <= "0100100"; -- 2
            when "0011" => segments <= "0110000"; -- 3
            when "0100" => segments <= "0011001"; -- 4
            when "0101" => segments <= "0010010"; -- 5
            when "0110" => segments <= "0000010"; -- 6
            when "0111" => segments <= "1111000"; -- 7
            when "1000" => segments <= "0000000"; -- 8
            when "1001" => segments <= "0010000"; -- 9
			when "1010" => segments <= "0001000"; -- A
			when "1011" => segments <= "0000011"; -- B
			when "1100" => segments <= "1000110"; -- C
			when "1101" => segments <= "0100001"; -- D
			when "1110" => segments <= "0000110"; -- E
			when "1111" => segments <= "0001110"; -- E
				
            when others => segments <= "0000000"; -- Default: all segments off
        end case;
    end process;
end Behavioral;
