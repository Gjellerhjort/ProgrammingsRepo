----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    11:53:25 05/25/2023 
-- Design Name: 
-- Module Name:    bytetx - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.all;
use IEEE.std_logic_unsigned.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity bytetx is
    Port ( clk : in  STD_LOGIC;
           inbyte : in  STD_LOGIC_VECTOR (7 downto 0);
		   l_clk : out std_logic;
           tx : out  STD_LOGIC);
end bytetx;

architecture Behavioral of bytetx is
signal count: std_logic_vector(3 downto 0):=(others => '0');
signal lclk: std_logic := '1';

begin

l_clk<=lclk;

process (clk)
begin  
   if (clk'event and clk = '1') then
	
	   if(count="0000") then
         tx <= '0' or (not lclk);
			count <= std_logic_vector(unsigned(count) + 1);
	   else
         if(unsigned(count)<9) then
		      tx <= inbyte(to_integer(unsigned(count)-1)) or (not lclk);
            count <= std_logic_vector(unsigned(count) + 1); 
		   else
		      tx <='1';
				if(unsigned(count)>11) then
				   count <= "0000";
					lclk <= not lclk;
				else
				   count <= std_logic_vector(unsigned(count) + 1);
				end if;
		   end if;
      end if;
   end if;    
end process;



end Behavioral;

