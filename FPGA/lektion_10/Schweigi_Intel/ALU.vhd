----------------------------------------------------------------------------------
-- Company: AAU
-- Engineer: Henrik Schiøler
-- 
-- Create Date: 07/20/2023 11:34:37 AM
-- Design Name: 
-- Module Name: ALU - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
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
USE IEEE.numeric_std.ALL;
USE ieee.std_logic_unsigned.ALL;



entity ALU is
    Port ( argA : in STD_LOGIC_VECTOR (7 downto 0);
           argB : in STD_LOGIC_VECTOR (7 downto 0);
           res : inout STD_LOGIC_VECTOR (7 downto 0);
           sel : in STD_LOGIC_VECTOR (3 downto 0);
           Z : out std_logic;
           C : out std_logic);
end ALU;

architecture Behavioral of ALU is
signal sum,diff,shiftL,shiftR,shiftLR,band,bor,bxor : std_logic_vector(7 downto 0);
signal flagDZ, flagDC, flagSZ, flagsC, flagshZ, flagshO : std_logic;

begin

diff <= std_logic_vector(unsigned(argA) - unsigned(argB)) when (unsigned(argA) > unsigned(argB)) else
         std_logic_vector(256 + unsigned(argA) - unsigned(argB)) when (unsigned(argA) < unsigned(argB)) else
         (others => '0');
        
flagDC <= '0' when (unsigned(argA) >= unsigned(argB)) else
         '1';
         
flagDZ <= '1' when (unsigned(argA) = unsigned(argB)) else
         '0';
           
sum <= std_logic_vector(unsigned(argA) + unsigned(argB));
        
flagSC <= '0' when (unsigned('0' & argA) + unsigned('0' & argB) < 256) else
         '1';
         
flagSZ <= '1' when (sum = 0) else
         '0';
         
shiftL <= std_logic_vector(shift_left(unsigned(argA), to_integer(unsigned(argB))));
shiftLR <= std_logic_vector(shift_right(unsigned(shiftL), to_integer(unsigned(argB)))); -- to check for overflow

flagshO <= '0' when (argA = shiftLR) else
           '1';

shiftR <= std_logic_vector(shift_right(unsigned(argA), to_integer(unsigned(argB))));
flagshZ <= '1' when (shiftR = "00000000") else
           '0';
           
band <= argA and argB;
bor <= argA or argB;
bxor <= argA xor argB;
         
with sel select
    res <= sum when "0000",
           diff when "0001",
           shiftL when "0010",
           shiftR when "0011",
           band when "0100",
           bor when "0101",
           bxor when "0110",
           (others => '0') when others;
           
with sel select
    C <= flagSC when "0000",
         flagDC when "0001",
         flagshO when "0010",
         '0' when "0011",
          '0' when others;
          
--with sel select
--    Z <= flagSZ when "0000",
--         flagDZ when "0001",
--         '0' when "0010",
--         flagshZ when "0011",
--         '0' when others;
         
Z <= '1' when res = "00000000" else
         '0';

end Behavioral;
