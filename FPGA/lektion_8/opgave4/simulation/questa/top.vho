-- Copyright (C) 2023  Intel Corporation. All rights reserved.
-- Your use of Intel Corporation's design tools, logic functions 
-- and other software and tools, and any partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Intel Program License 
-- Subscription Agreement, the Intel Quartus Prime License Agreement,
-- the Intel FPGA IP License Agreement, or other applicable license
-- agreement, including, without limitation, that your use is for
-- the sole purpose of programming logic devices manufactured by
-- Intel and sold by Intel or its authorized distributors.  Please
-- refer to the applicable agreement for further details, at
-- https://fpgasoftware.intel.com/eula.

-- VENDOR "Altera"
-- PROGRAM "Quartus Prime"
-- VERSION "Version 23.1std.0 Build 991 11/28/2023 SC Lite Edition"

-- DATE "01/05/2025 18:01:15"

-- 
-- Device: Altera 5CEBA4F23C7 Package FBGA484
-- 

-- 
-- This VHDL file should be used for Questa Intel FPGA (VHDL) only
-- 

LIBRARY ALTERA_LNSIM;
LIBRARY CYCLONEV;
LIBRARY IEEE;
USE ALTERA_LNSIM.ALTERA_LNSIM_COMPONENTS.ALL;
USE CYCLONEV.CYCLONEV_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY 	MemoryBlockArray IS
    PORT (
	a : IN std_logic_vector(3 DOWNTO 0);
	b : BUFFER std_logic_vector(3 DOWNTO 0);
	addr : IN std_logic_vector(1 DOWNTO 0);
	rd : IN std_logic;
	wr : IN std_logic
	);
END MemoryBlockArray;

-- Design Ports Information
-- b[0]	=>  Location: PIN_L18,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[1]	=>  Location: PIN_P16,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[2]	=>  Location: PIN_L17,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[3]	=>  Location: PIN_P19,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- addr[0]	=>  Location: PIN_M22,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- addr[1]	=>  Location: PIN_K21,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- rd	=>  Location: PIN_M16,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[0]	=>  Location: PIN_M18,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- wr	=>  Location: PIN_N19,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[1]	=>  Location: PIN_N16,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[2]	=>  Location: PIN_L19,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[3]	=>  Location: PIN_L22,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF MemoryBlockArray IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_a : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_b : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_addr : std_logic_vector(1 DOWNTO 0);
SIGNAL ww_rd : std_logic;
SIGNAL ww_wr : std_logic;
SIGNAL \~QUARTUS_CREATED_GND~I_combout\ : std_logic;
SIGNAL \a[0]~input_o\ : std_logic;
SIGNAL \addr[1]~input_o\ : std_logic;
SIGNAL \wr~input_o\ : std_logic;
SIGNAL \addr[0]~input_o\ : std_logic;
SIGNAL \rtl~3_combout\ : std_logic;
SIGNAL \memory~12_combout\ : std_logic;
SIGNAL \rtl~1_combout\ : std_logic;
SIGNAL \memory~4_combout\ : std_logic;
SIGNAL \rtl~2_combout\ : std_logic;
SIGNAL \memory~8_combout\ : std_logic;
SIGNAL \rtl~0_combout\ : std_logic;
SIGNAL \memory~0_combout\ : std_logic;
SIGNAL \memory~16_combout\ : std_logic;
SIGNAL \rd~input_o\ : std_logic;
SIGNAL \a[1]~input_o\ : std_logic;
SIGNAL \memory~5_combout\ : std_logic;
SIGNAL \memory~13_combout\ : std_logic;
SIGNAL \memory~1_combout\ : std_logic;
SIGNAL \memory~9_combout\ : std_logic;
SIGNAL \memory~17_combout\ : std_logic;
SIGNAL \a[2]~input_o\ : std_logic;
SIGNAL \memory~2_combout\ : std_logic;
SIGNAL \memory~14_combout\ : std_logic;
SIGNAL \memory~10_combout\ : std_logic;
SIGNAL \memory~6_combout\ : std_logic;
SIGNAL \memory~18_combout\ : std_logic;
SIGNAL \a[3]~input_o\ : std_logic;
SIGNAL \memory~3_combout\ : std_logic;
SIGNAL \memory~7_combout\ : std_logic;
SIGNAL \memory~15_combout\ : std_logic;
SIGNAL \memory~11_combout\ : std_logic;
SIGNAL \memory~19_combout\ : std_logic;
SIGNAL \ALT_INV_a[3]~input_o\ : std_logic;
SIGNAL \ALT_INV_a[2]~input_o\ : std_logic;
SIGNAL \ALT_INV_a[1]~input_o\ : std_logic;
SIGNAL \ALT_INV_wr~input_o\ : std_logic;
SIGNAL \ALT_INV_a[0]~input_o\ : std_logic;
SIGNAL \ALT_INV_rd~input_o\ : std_logic;
SIGNAL \ALT_INV_addr[1]~input_o\ : std_logic;
SIGNAL \ALT_INV_addr[0]~input_o\ : std_logic;
SIGNAL \ALT_INV_memory~15_combout\ : std_logic;
SIGNAL \ALT_INV_memory~11_combout\ : std_logic;
SIGNAL \ALT_INV_memory~7_combout\ : std_logic;
SIGNAL \ALT_INV_memory~3_combout\ : std_logic;
SIGNAL \ALT_INV_memory~14_combout\ : std_logic;
SIGNAL \ALT_INV_memory~10_combout\ : std_logic;
SIGNAL \ALT_INV_memory~6_combout\ : std_logic;
SIGNAL \ALT_INV_memory~2_combout\ : std_logic;
SIGNAL \ALT_INV_memory~13_combout\ : std_logic;
SIGNAL \ALT_INV_memory~9_combout\ : std_logic;
SIGNAL \ALT_INV_memory~5_combout\ : std_logic;
SIGNAL \ALT_INV_memory~1_combout\ : std_logic;
SIGNAL \ALT_INV_memory~12_combout\ : std_logic;
SIGNAL \ALT_INV_memory~8_combout\ : std_logic;
SIGNAL \ALT_INV_memory~4_combout\ : std_logic;
SIGNAL \ALT_INV_memory~0_combout\ : std_logic;
SIGNAL \ALT_INV_rtl~3_combout\ : std_logic;
SIGNAL \ALT_INV_rtl~2_combout\ : std_logic;
SIGNAL \ALT_INV_rtl~1_combout\ : std_logic;
SIGNAL \ALT_INV_rtl~0_combout\ : std_logic;

BEGIN

ww_a <= a;
b <= ww_b;
ww_addr <= addr;
ww_rd <= rd;
ww_wr <= wr;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_a[3]~input_o\ <= NOT \a[3]~input_o\;
\ALT_INV_a[2]~input_o\ <= NOT \a[2]~input_o\;
\ALT_INV_a[1]~input_o\ <= NOT \a[1]~input_o\;
\ALT_INV_wr~input_o\ <= NOT \wr~input_o\;
\ALT_INV_a[0]~input_o\ <= NOT \a[0]~input_o\;
\ALT_INV_rd~input_o\ <= NOT \rd~input_o\;
\ALT_INV_addr[1]~input_o\ <= NOT \addr[1]~input_o\;
\ALT_INV_addr[0]~input_o\ <= NOT \addr[0]~input_o\;
\ALT_INV_memory~15_combout\ <= NOT \memory~15_combout\;
\ALT_INV_memory~11_combout\ <= NOT \memory~11_combout\;
\ALT_INV_memory~7_combout\ <= NOT \memory~7_combout\;
\ALT_INV_memory~3_combout\ <= NOT \memory~3_combout\;
\ALT_INV_memory~14_combout\ <= NOT \memory~14_combout\;
\ALT_INV_memory~10_combout\ <= NOT \memory~10_combout\;
\ALT_INV_memory~6_combout\ <= NOT \memory~6_combout\;
\ALT_INV_memory~2_combout\ <= NOT \memory~2_combout\;
\ALT_INV_memory~13_combout\ <= NOT \memory~13_combout\;
\ALT_INV_memory~9_combout\ <= NOT \memory~9_combout\;
\ALT_INV_memory~5_combout\ <= NOT \memory~5_combout\;
\ALT_INV_memory~1_combout\ <= NOT \memory~1_combout\;
\ALT_INV_memory~12_combout\ <= NOT \memory~12_combout\;
\ALT_INV_memory~8_combout\ <= NOT \memory~8_combout\;
\ALT_INV_memory~4_combout\ <= NOT \memory~4_combout\;
\ALT_INV_memory~0_combout\ <= NOT \memory~0_combout\;
\ALT_INV_rtl~3_combout\ <= NOT \rtl~3_combout\;
\ALT_INV_rtl~2_combout\ <= NOT \rtl~2_combout\;
\ALT_INV_rtl~1_combout\ <= NOT \rtl~1_combout\;
\ALT_INV_rtl~0_combout\ <= NOT \rtl~0_combout\;

-- Location: IOOBUF_X54_Y21_N22
\b[0]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \memory~16_combout\,
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(0));

-- Location: IOOBUF_X54_Y17_N5
\b[1]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \memory~17_combout\,
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(1));

-- Location: IOOBUF_X54_Y20_N22
\b[2]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \memory~18_combout\,
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(2));

-- Location: IOOBUF_X54_Y17_N39
\b[3]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \memory~19_combout\,
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(3));

-- Location: IOIBUF_X54_Y19_N21
\a[0]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(0),
	o => \a[0]~input_o\);

-- Location: IOIBUF_X54_Y21_N38
\addr[1]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_addr(1),
	o => \addr[1]~input_o\);

-- Location: IOIBUF_X54_Y19_N4
\wr~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_wr,
	o => \wr~input_o\);

-- Location: IOIBUF_X54_Y19_N38
\addr[0]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_addr(0),
	o => \addr[0]~input_o\);

-- Location: LABCELL_X53_Y19_N45
\rtl~3\ : cyclonev_lcell_comb
-- Equation(s):
-- \rtl~3_combout\ = ( \addr[0]~input_o\ & ( (\addr[1]~input_o\ & !\wr~input_o\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000000000000000000000000000001111000000000000111100000000",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_addr[1]~input_o\,
	datad => \ALT_INV_wr~input_o\,
	dataf => \ALT_INV_addr[0]~input_o\,
	combout => \rtl~3_combout\);

-- Location: LABCELL_X53_Y19_N21
\memory~12\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~12_combout\ = ( \memory~12_combout\ & ( (!\rtl~3_combout\) # (\a[0]~input_o\) ) ) # ( !\memory~12_combout\ & ( (\a[0]~input_o\ & \rtl~3_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000001010101000000000101010111111111010101011111111101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[0]~input_o\,
	datad => \ALT_INV_rtl~3_combout\,
	dataf => \ALT_INV_memory~12_combout\,
	combout => \memory~12_combout\);

-- Location: LABCELL_X53_Y19_N15
\rtl~1\ : cyclonev_lcell_comb
-- Equation(s):
-- \rtl~1_combout\ = ( \addr[0]~input_o\ & ( (!\addr[1]~input_o\ & !\wr~input_o\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000000000000000000000000011110000000000001111000000000000",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_addr[1]~input_o\,
	datad => \ALT_INV_wr~input_o\,
	dataf => \ALT_INV_addr[0]~input_o\,
	combout => \rtl~1_combout\);

-- Location: LABCELL_X53_Y19_N18
\memory~4\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~4_combout\ = ( \memory~4_combout\ & ( (!\rtl~1_combout\) # (\a[0]~input_o\) ) ) # ( !\memory~4_combout\ & ( (\a[0]~input_o\ & \rtl~1_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0001000100010001000100010001000111011101110111011101110111011101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[0]~input_o\,
	datab => \ALT_INV_rtl~1_combout\,
	dataf => \ALT_INV_memory~4_combout\,
	combout => \memory~4_combout\);

-- Location: LABCELL_X53_Y19_N57
\rtl~2\ : cyclonev_lcell_comb
-- Equation(s):
-- \rtl~2_combout\ = ( !\addr[0]~input_o\ & ( (\addr[1]~input_o\ & !\wr~input_o\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000111100000000000011110000000000000000000000000000000000000000",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_addr[1]~input_o\,
	datad => \ALT_INV_wr~input_o\,
	dataf => \ALT_INV_addr[0]~input_o\,
	combout => \rtl~2_combout\);

-- Location: LABCELL_X53_Y19_N3
\memory~8\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~8_combout\ = ( \rtl~2_combout\ & ( \a[0]~input_o\ ) ) # ( !\rtl~2_combout\ & ( \memory~8_combout\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000011111111000000001111111101010101010101010101010101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[0]~input_o\,
	datad => \ALT_INV_memory~8_combout\,
	dataf => \ALT_INV_rtl~2_combout\,
	combout => \memory~8_combout\);

-- Location: LABCELL_X53_Y19_N51
\rtl~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \rtl~0_combout\ = ( \addr[0]~input_o\ ) # ( !\addr[0]~input_o\ & ( (\wr~input_o\) # (\addr[1]~input_o\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000111111111111000011111111111111111111111111111111111111111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_addr[1]~input_o\,
	datad => \ALT_INV_wr~input_o\,
	dataf => \ALT_INV_addr[0]~input_o\,
	combout => \rtl~0_combout\);

-- Location: LABCELL_X53_Y19_N0
\memory~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~0_combout\ = ( \rtl~0_combout\ & ( \memory~0_combout\ ) ) # ( !\rtl~0_combout\ & ( \a[0]~input_o\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101010101010101010101010101010100000000111111110000000011111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[0]~input_o\,
	datad => \ALT_INV_memory~0_combout\,
	dataf => \ALT_INV_rtl~0_combout\,
	combout => \memory~0_combout\);

-- Location: LABCELL_X52_Y19_N33
\memory~16\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~16_combout\ = ( \addr[0]~input_o\ & ( \memory~0_combout\ & ( (!\addr[1]~input_o\ & ((\memory~4_combout\))) # (\addr[1]~input_o\ & (\memory~12_combout\)) ) ) ) # ( !\addr[0]~input_o\ & ( \memory~0_combout\ & ( (!\addr[1]~input_o\) # 
-- (\memory~8_combout\) ) ) ) # ( \addr[0]~input_o\ & ( !\memory~0_combout\ & ( (!\addr[1]~input_o\ & ((\memory~4_combout\))) # (\addr[1]~input_o\ & (\memory~12_combout\)) ) ) ) # ( !\addr[0]~input_o\ & ( !\memory~0_combout\ & ( (\memory~8_combout\ & 
-- \addr[1]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000001111001100110101010111111111000011110011001101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_memory~12_combout\,
	datab => \ALT_INV_memory~4_combout\,
	datac => \ALT_INV_memory~8_combout\,
	datad => \ALT_INV_addr[1]~input_o\,
	datae => \ALT_INV_addr[0]~input_o\,
	dataf => \ALT_INV_memory~0_combout\,
	combout => \memory~16_combout\);

-- Location: IOIBUF_X54_Y18_N61
\rd~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_rd,
	o => \rd~input_o\);

-- Location: IOIBUF_X54_Y18_N44
\a[1]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(1),
	o => \a[1]~input_o\);

-- Location: LABCELL_X53_Y19_N12
\memory~5\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~5_combout\ = ( \memory~5_combout\ & ( (!\rtl~1_combout\) # (\a[1]~input_o\) ) ) # ( !\memory~5_combout\ & ( (\rtl~1_combout\ & \a[1]~input_o\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000110011000000000011001111001100111111111100110011111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_rtl~1_combout\,
	datad => \ALT_INV_a[1]~input_o\,
	dataf => \ALT_INV_memory~5_combout\,
	combout => \memory~5_combout\);

-- Location: LABCELL_X53_Y19_N42
\memory~13\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~13_combout\ = ( \memory~13_combout\ & ( (!\rtl~3_combout\) # (\a[1]~input_o\) ) ) # ( !\memory~13_combout\ & ( (\a[1]~input_o\ & \rtl~3_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000110011000000000011001111111111001100111111111100110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_a[1]~input_o\,
	datad => \ALT_INV_rtl~3_combout\,
	dataf => \ALT_INV_memory~13_combout\,
	combout => \memory~13_combout\);

-- Location: LABCELL_X53_Y19_N48
\memory~1\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~1_combout\ = ( \rtl~0_combout\ & ( \memory~1_combout\ ) ) # ( !\rtl~0_combout\ & ( \a[1]~input_o\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011001100110011001100110011001100001111000011110000111100001111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_a[1]~input_o\,
	datac => \ALT_INV_memory~1_combout\,
	dataf => \ALT_INV_rtl~0_combout\,
	combout => \memory~1_combout\);

-- Location: LABCELL_X53_Y19_N54
\memory~9\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~9_combout\ = ( \rtl~2_combout\ & ( \a[1]~input_o\ ) ) # ( !\rtl~2_combout\ & ( \memory~9_combout\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000011111111000000001111111100110011001100110011001100110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_a[1]~input_o\,
	datad => \ALT_INV_memory~9_combout\,
	dataf => \ALT_INV_rtl~2_combout\,
	combout => \memory~9_combout\);

-- Location: LABCELL_X52_Y19_N36
\memory~17\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~17_combout\ = ( \memory~1_combout\ & ( \memory~9_combout\ & ( (!\addr[0]~input_o\) # ((!\addr[1]~input_o\ & (\memory~5_combout\)) # (\addr[1]~input_o\ & ((\memory~13_combout\)))) ) ) ) # ( !\memory~1_combout\ & ( \memory~9_combout\ & ( 
-- (!\addr[1]~input_o\ & (\memory~5_combout\ & (\addr[0]~input_o\))) # (\addr[1]~input_o\ & (((!\addr[0]~input_o\) # (\memory~13_combout\)))) ) ) ) # ( \memory~1_combout\ & ( !\memory~9_combout\ & ( (!\addr[1]~input_o\ & (((!\addr[0]~input_o\)) # 
-- (\memory~5_combout\))) # (\addr[1]~input_o\ & (((\addr[0]~input_o\ & \memory~13_combout\)))) ) ) ) # ( !\memory~1_combout\ & ( !\memory~9_combout\ & ( (\addr[0]~input_o\ & ((!\addr[1]~input_o\ & (\memory~5_combout\)) # (\addr[1]~input_o\ & 
-- ((\memory~13_combout\))))) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000001000000111101000101010011101010010010101111111001011110111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_addr[1]~input_o\,
	datab => \ALT_INV_memory~5_combout\,
	datac => \ALT_INV_addr[0]~input_o\,
	datad => \ALT_INV_memory~13_combout\,
	datae => \ALT_INV_memory~1_combout\,
	dataf => \ALT_INV_memory~9_combout\,
	combout => \memory~17_combout\);

-- Location: IOIBUF_X54_Y21_N4
\a[2]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(2),
	o => \a[2]~input_o\);

-- Location: LABCELL_X53_Y19_N6
\memory~2\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~2_combout\ = ( \memory~2_combout\ & ( (\rtl~0_combout\) # (\a[2]~input_o\) ) ) # ( !\memory~2_combout\ & ( (\a[2]~input_o\ & !\rtl~0_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101000001010000010100000101000001011111010111110101111101011111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[2]~input_o\,
	datac => \ALT_INV_rtl~0_combout\,
	dataf => \ALT_INV_memory~2_combout\,
	combout => \memory~2_combout\);

-- Location: LABCELL_X53_Y19_N33
\memory~14\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~14_combout\ = ( \memory~14_combout\ & ( (!\rtl~3_combout\) # (\a[2]~input_o\) ) ) # ( !\memory~14_combout\ & ( (\a[2]~input_o\ & \rtl~3_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000001010101000000000101010111111111010101011111111101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[2]~input_o\,
	datad => \ALT_INV_rtl~3_combout\,
	dataf => \ALT_INV_memory~14_combout\,
	combout => \memory~14_combout\);

-- Location: LABCELL_X53_Y19_N30
\memory~10\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~10_combout\ = ( \memory~10_combout\ & ( (!\rtl~2_combout\) # (\a[2]~input_o\) ) ) # ( !\memory~10_combout\ & ( (\a[2]~input_o\ & \rtl~2_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000001010101000000000101010111111111010101011111111101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[2]~input_o\,
	datad => \ALT_INV_rtl~2_combout\,
	dataf => \ALT_INV_memory~10_combout\,
	combout => \memory~10_combout\);

-- Location: LABCELL_X53_Y19_N9
\memory~6\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~6_combout\ = ( \memory~6_combout\ & ( (!\rtl~1_combout\) # (\a[2]~input_o\) ) ) # ( !\memory~6_combout\ & ( (\a[2]~input_o\ & \rtl~1_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000010100000101000001010000010111110101111101011111010111110101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[2]~input_o\,
	datac => \ALT_INV_rtl~1_combout\,
	dataf => \ALT_INV_memory~6_combout\,
	combout => \memory~6_combout\);

-- Location: LABCELL_X52_Y19_N12
\memory~18\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~18_combout\ = ( \addr[1]~input_o\ & ( \memory~6_combout\ & ( (!\addr[0]~input_o\ & ((\memory~10_combout\))) # (\addr[0]~input_o\ & (\memory~14_combout\)) ) ) ) # ( !\addr[1]~input_o\ & ( \memory~6_combout\ & ( (\addr[0]~input_o\) # 
-- (\memory~2_combout\) ) ) ) # ( \addr[1]~input_o\ & ( !\memory~6_combout\ & ( (!\addr[0]~input_o\ & ((\memory~10_combout\))) # (\addr[0]~input_o\ & (\memory~14_combout\)) ) ) ) # ( !\addr[1]~input_o\ & ( !\memory~6_combout\ & ( (\memory~2_combout\ & 
-- !\addr[0]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101000001010000000000111111001101011111010111110000001111110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_memory~2_combout\,
	datab => \ALT_INV_memory~14_combout\,
	datac => \ALT_INV_addr[0]~input_o\,
	datad => \ALT_INV_memory~10_combout\,
	datae => \ALT_INV_addr[1]~input_o\,
	dataf => \ALT_INV_memory~6_combout\,
	combout => \memory~18_combout\);

-- Location: IOIBUF_X54_Y19_N55
\a[3]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(3),
	o => \a[3]~input_o\);

-- Location: LABCELL_X53_Y19_N39
\memory~3\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~3_combout\ = ( \rtl~0_combout\ & ( \memory~3_combout\ ) ) # ( !\rtl~0_combout\ & ( \a[3]~input_o\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101010101010101010101010101010100001111000011110000111100001111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[3]~input_o\,
	datac => \ALT_INV_memory~3_combout\,
	dataf => \ALT_INV_rtl~0_combout\,
	combout => \memory~3_combout\);

-- Location: LABCELL_X53_Y19_N24
\memory~7\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~7_combout\ = ( \memory~7_combout\ & ( (!\rtl~1_combout\) # (\a[3]~input_o\) ) ) # ( !\memory~7_combout\ & ( (\a[3]~input_o\ & \rtl~1_combout\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000001111000000000000111111111111000011111111111100001111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_a[3]~input_o\,
	datad => \ALT_INV_rtl~1_combout\,
	dataf => \ALT_INV_memory~7_combout\,
	combout => \memory~7_combout\);

-- Location: LABCELL_X52_Y19_N27
\memory~15\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~15_combout\ = ( \memory~15_combout\ & ( \rtl~3_combout\ & ( \a[3]~input_o\ ) ) ) # ( !\memory~15_combout\ & ( \rtl~3_combout\ & ( \a[3]~input_o\ ) ) ) # ( \memory~15_combout\ & ( !\rtl~3_combout\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000000000111111111111111100001111000011110000111100001111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_a[3]~input_o\,
	datae => \ALT_INV_memory~15_combout\,
	dataf => \ALT_INV_rtl~3_combout\,
	combout => \memory~15_combout\);

-- Location: LABCELL_X53_Y19_N36
\memory~11\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~11_combout\ = ( \rtl~2_combout\ & ( \a[3]~input_o\ ) ) # ( !\rtl~2_combout\ & ( \memory~11_combout\ ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000011111111000000001111111101010101010101010101010101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[3]~input_o\,
	datad => \ALT_INV_memory~11_combout\,
	dataf => \ALT_INV_rtl~2_combout\,
	combout => \memory~11_combout\);

-- Location: LABCELL_X52_Y19_N18
\memory~19\ : cyclonev_lcell_comb
-- Equation(s):
-- \memory~19_combout\ = ( \addr[1]~input_o\ & ( \memory~11_combout\ & ( (!\addr[0]~input_o\) # (\memory~15_combout\) ) ) ) # ( !\addr[1]~input_o\ & ( \memory~11_combout\ & ( (!\addr[0]~input_o\ & (\memory~3_combout\)) # (\addr[0]~input_o\ & 
-- ((\memory~7_combout\))) ) ) ) # ( \addr[1]~input_o\ & ( !\memory~11_combout\ & ( (\addr[0]~input_o\ & \memory~15_combout\) ) ) ) # ( !\addr[1]~input_o\ & ( !\memory~11_combout\ & ( (!\addr[0]~input_o\ & (\memory~3_combout\)) # (\addr[0]~input_o\ & 
-- ((\memory~7_combout\))) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101001101010011000000000000111101010011010100111111000011111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_memory~3_combout\,
	datab => \ALT_INV_memory~7_combout\,
	datac => \ALT_INV_addr[0]~input_o\,
	datad => \ALT_INV_memory~15_combout\,
	datae => \ALT_INV_addr[1]~input_o\,
	dataf => \ALT_INV_memory~11_combout\,
	combout => \memory~19_combout\);

-- Location: LABCELL_X48_Y8_N0
\~QUARTUS_CREATED_GND~I\ : cyclonev_lcell_comb
-- Equation(s):

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000000000000000000000000000000000000000000000000000000000",
	shared_arith => "off")
-- pragma translate_on
;
END structure;


