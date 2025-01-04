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

-- DATE "01/05/2025 00:12:20"

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

ENTITY 	MemoryBlock4 IS
    PORT (
	a : IN std_logic_vector(3 DOWNTO 0);
	b : BUFFER std_logic_vector(3 DOWNTO 0);
	rd : IN std_logic;
	wr : IN std_logic
	);
END MemoryBlock4;

-- Design Ports Information
-- b[0]	=>  Location: PIN_R6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[1]	=>  Location: PIN_R5,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[2]	=>  Location: PIN_U8,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b[3]	=>  Location: PIN_U7,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- rd	=>  Location: PIN_V10,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[0]	=>  Location: PIN_N2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- wr	=>  Location: PIN_G1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[1]	=>  Location: PIN_C2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[2]	=>  Location: PIN_C1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a[3]	=>  Location: PIN_G2,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF MemoryBlock4 IS
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
SIGNAL ww_rd : std_logic;
SIGNAL ww_wr : std_logic;
SIGNAL \~QUARTUS_CREATED_GND~I_combout\ : std_logic;
SIGNAL \a[0]~input_o\ : std_logic;
SIGNAL \wr~input_o\ : std_logic;
SIGNAL \rd~input_o\ : std_logic;
SIGNAL \a[1]~input_o\ : std_logic;
SIGNAL \a[2]~input_o\ : std_logic;
SIGNAL \a[3]~input_o\ : std_logic;
SIGNAL memory : std_logic_vector(3 DOWNTO 0);
SIGNAL \ALT_INV_a[3]~input_o\ : std_logic;
SIGNAL \ALT_INV_a[2]~input_o\ : std_logic;
SIGNAL \ALT_INV_a[1]~input_o\ : std_logic;
SIGNAL \ALT_INV_wr~input_o\ : std_logic;
SIGNAL \ALT_INV_a[0]~input_o\ : std_logic;
SIGNAL \ALT_INV_rd~input_o\ : std_logic;
SIGNAL ALT_INV_memory : std_logic_vector(3 DOWNTO 0);

BEGIN

ww_a <= a;
b <= ww_b;
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
ALT_INV_memory(3) <= NOT memory(3);
ALT_INV_memory(2) <= NOT memory(2);
ALT_INV_memory(1) <= NOT memory(1);
ALT_INV_memory(0) <= NOT memory(0);

-- Location: IOOBUF_X10_Y0_N59
\b[0]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => memory(0),
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(0));

-- Location: IOOBUF_X10_Y0_N42
\b[1]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => memory(1),
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(1));

-- Location: IOOBUF_X10_Y0_N76
\b[2]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => memory(2),
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(2));

-- Location: IOOBUF_X10_Y0_N93
\b[3]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => memory(3),
	oe => \ALT_INV_rd~input_o\,
	devoe => ww_devoe,
	o => ww_b(3));

-- Location: IOIBUF_X0_Y19_N38
\a[0]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(0),
	o => \a[0]~input_o\);

-- Location: IOIBUF_X0_Y21_N21
\wr~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_wr,
	o => \wr~input_o\);

-- Location: LABCELL_X1_Y21_N30
\memory[0]\ : cyclonev_lcell_comb
-- Equation(s):
-- memory(0) = ( \wr~input_o\ & ( memory(0) ) ) # ( !\wr~input_o\ & ( memory(0) & ( \a[0]~input_o\ ) ) ) # ( !\wr~input_o\ & ( !memory(0) & ( \a[0]~input_o\ ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000111100001111000000000000000000001111000011111111111111111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datac => \ALT_INV_a[0]~input_o\,
	datae => \ALT_INV_wr~input_o\,
	dataf => ALT_INV_memory(0),
	combout => memory(0));

-- Location: IOIBUF_X16_Y0_N41
\rd~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_rd,
	o => \rd~input_o\);

-- Location: IOIBUF_X0_Y21_N38
\a[1]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(1),
	o => \a[1]~input_o\);

-- Location: LABCELL_X1_Y21_N6
\memory[1]\ : cyclonev_lcell_comb
-- Equation(s):
-- memory(1) = ( \wr~input_o\ & ( memory(1) ) ) # ( !\wr~input_o\ & ( memory(1) & ( \a[1]~input_o\ ) ) ) # ( !\wr~input_o\ & ( !memory(1) & ( \a[1]~input_o\ ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011001100110011000000000000000000110011001100111111111111111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_a[1]~input_o\,
	datae => \ALT_INV_wr~input_o\,
	dataf => ALT_INV_memory(1),
	combout => memory(1));

-- Location: IOIBUF_X0_Y21_N55
\a[2]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(2),
	o => \a[2]~input_o\);

-- Location: LABCELL_X1_Y21_N15
\memory[2]\ : cyclonev_lcell_comb
-- Equation(s):
-- memory(2) = ( \wr~input_o\ & ( memory(2) ) ) # ( !\wr~input_o\ & ( memory(2) & ( \a[2]~input_o\ ) ) ) # ( !\wr~input_o\ & ( !memory(2) & ( \a[2]~input_o\ ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101010101010101000000000000000001010101010101011111111111111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[2]~input_o\,
	datae => \ALT_INV_wr~input_o\,
	dataf => ALT_INV_memory(2),
	combout => memory(2));

-- Location: IOIBUF_X0_Y21_N4
\a[3]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a(3),
	o => \a[3]~input_o\);

-- Location: LABCELL_X1_Y21_N51
\memory[3]\ : cyclonev_lcell_comb
-- Equation(s):
-- memory(3) = ( \wr~input_o\ & ( memory(3) ) ) # ( !\wr~input_o\ & ( memory(3) & ( \a[3]~input_o\ ) ) ) # ( !\wr~input_o\ & ( !memory(3) & ( \a[3]~input_o\ ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101010101010101000000000000000001010101010101011111111111111111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_a[3]~input_o\,
	datae => \ALT_INV_wr~input_o\,
	dataf => ALT_INV_memory(3),
	combout => memory(3));

-- Location: MLABCELL_X45_Y13_N0
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


