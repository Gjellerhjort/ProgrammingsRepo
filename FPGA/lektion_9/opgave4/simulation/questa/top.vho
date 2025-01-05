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

-- DATE "01/05/2025 14:34:10"

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

ENTITY 	icelection9 IS
    PORT (
	binary_in : IN std_logic_vector(3 DOWNTO 0);
	segments : BUFFER std_logic_vector(6 DOWNTO 0)
	);
END icelection9;

-- Design Ports Information
-- segments[0]	=>  Location: PIN_U2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- segments[1]	=>  Location: PIN_U1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- segments[2]	=>  Location: PIN_C2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- segments[3]	=>  Location: PIN_N1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- segments[4]	=>  Location: PIN_G2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- segments[5]	=>  Location: PIN_AA1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- segments[6]	=>  Location: PIN_W2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- binary_in[0]	=>  Location: PIN_D3,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- binary_in[1]	=>  Location: PIN_L2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- binary_in[2]	=>  Location: PIN_E2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- binary_in[3]	=>  Location: PIN_N2,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF icelection9 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_binary_in : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_segments : std_logic_vector(6 DOWNTO 0);
SIGNAL \~QUARTUS_CREATED_GND~I_combout\ : std_logic;
SIGNAL \binary_in[3]~input_o\ : std_logic;
SIGNAL \binary_in[2]~input_o\ : std_logic;
SIGNAL \binary_in[0]~input_o\ : std_logic;
SIGNAL \binary_in[1]~input_o\ : std_logic;
SIGNAL \Mux6~0_combout\ : std_logic;
SIGNAL \Mux5~0_combout\ : std_logic;
SIGNAL \Mux4~0_combout\ : std_logic;
SIGNAL \Mux3~0_combout\ : std_logic;
SIGNAL \Mux2~0_combout\ : std_logic;
SIGNAL \Mux1~0_combout\ : std_logic;
SIGNAL \Mux0~0_combout\ : std_logic;
SIGNAL \ALT_INV_binary_in[3]~input_o\ : std_logic;
SIGNAL \ALT_INV_binary_in[2]~input_o\ : std_logic;
SIGNAL \ALT_INV_binary_in[1]~input_o\ : std_logic;
SIGNAL \ALT_INV_binary_in[0]~input_o\ : std_logic;
SIGNAL \ALT_INV_Mux0~0_combout\ : std_logic;

BEGIN

ww_binary_in <= binary_in;
segments <= ww_segments;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_binary_in[3]~input_o\ <= NOT \binary_in[3]~input_o\;
\ALT_INV_binary_in[2]~input_o\ <= NOT \binary_in[2]~input_o\;
\ALT_INV_binary_in[1]~input_o\ <= NOT \binary_in[1]~input_o\;
\ALT_INV_binary_in[0]~input_o\ <= NOT \binary_in[0]~input_o\;
\ALT_INV_Mux0~0_combout\ <= NOT \Mux0~0_combout\;

-- Location: IOOBUF_X0_Y19_N5
\segments[0]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux6~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(0));

-- Location: IOOBUF_X0_Y19_N22
\segments[1]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux5~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(1));

-- Location: IOOBUF_X0_Y21_N39
\segments[2]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux4~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(2));

-- Location: IOOBUF_X0_Y19_N56
\segments[3]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux3~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(3));

-- Location: IOOBUF_X0_Y21_N5
\segments[4]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux2~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(4));

-- Location: IOOBUF_X0_Y18_N96
\segments[5]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \Mux1~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(5));

-- Location: IOOBUF_X0_Y18_N62
\segments[6]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \ALT_INV_Mux0~0_combout\,
	devoe => ww_devoe,
	o => ww_segments(6));

-- Location: IOIBUF_X0_Y19_N38
\binary_in[3]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_binary_in(3),
	o => \binary_in[3]~input_o\);

-- Location: IOIBUF_X0_Y20_N21
\binary_in[2]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_binary_in(2),
	o => \binary_in[2]~input_o\);

-- Location: IOIBUF_X0_Y20_N4
\binary_in[0]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_binary_in(0),
	o => \binary_in[0]~input_o\);

-- Location: IOIBUF_X0_Y20_N38
\binary_in[1]~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_binary_in(1),
	o => \binary_in[1]~input_o\);

-- Location: LABCELL_X1_Y19_N0
\Mux6~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux6~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( (\binary_in[3]~input_o\ & !\binary_in[2]~input_o\) ) ) ) # ( \binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( !\binary_in[3]~input_o\ $ (\binary_in[2]~input_o\) ) ) ) # ( 
-- !\binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( (!\binary_in[3]~input_o\ & \binary_in[2]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000110000001100110000111100001100000000000000000011000000110000",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_binary_in[3]~input_o\,
	datac => \ALT_INV_binary_in[2]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux6~0_combout\);

-- Location: LABCELL_X1_Y19_N9
\Mux5~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux5~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( \binary_in[3]~input_o\ ) ) ) # ( !\binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( \binary_in[2]~input_o\ ) ) ) # ( \binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( 
-- (\binary_in[2]~input_o\ & !\binary_in[3]~input_o\) ) ) ) # ( !\binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( (\binary_in[2]~input_o\ & \binary_in[3]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000010100000101010100000101000001010101010101010000111100001111",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_binary_in[2]~input_o\,
	datac => \ALT_INV_binary_in[3]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux5~0_combout\);

-- Location: LABCELL_X1_Y19_N12
\Mux4~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux4~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( (\binary_in[3]~input_o\ & \binary_in[2]~input_o\) ) ) ) # ( !\binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( !\binary_in[3]~input_o\ $ (\binary_in[2]~input_o\) ) ) ) # ( 
-- !\binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( (\binary_in[3]~input_o\ & \binary_in[2]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000001100000011000000000000000011000011110000110000001100000011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_binary_in[3]~input_o\,
	datac => \ALT_INV_binary_in[2]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux4~0_combout\);

-- Location: LABCELL_X1_Y19_N21
\Mux3~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux3~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( \binary_in[2]~input_o\ ) ) ) # ( !\binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( (!\binary_in[2]~input_o\ & \binary_in[3]~input_o\) ) ) ) # ( \binary_in[0]~input_o\ & ( 
-- !\binary_in[1]~input_o\ & ( (!\binary_in[2]~input_o\ & !\binary_in[3]~input_o\) ) ) ) # ( !\binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( (\binary_in[2]~input_o\ & !\binary_in[3]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0101000001010000101000001010000000001010000010100101010101010101",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_binary_in[2]~input_o\,
	datac => \ALT_INV_binary_in[3]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux3~0_combout\);

-- Location: LABCELL_X1_Y19_N54
\Mux2~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux2~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( !\binary_in[3]~input_o\ ) ) ) # ( \binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( (!\binary_in[3]~input_o\) # (!\binary_in[2]~input_o\) ) ) ) # ( !\binary_in[0]~input_o\ & ( 
-- !\binary_in[1]~input_o\ & ( (!\binary_in[3]~input_o\ & \binary_in[2]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000110000001100111111001111110000000000000000001100110011001100",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_binary_in[3]~input_o\,
	datac => \ALT_INV_binary_in[2]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux2~0_combout\);

-- Location: LABCELL_X1_Y19_N33
\Mux1~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux1~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( !\binary_in[3]~input_o\ ) ) ) # ( !\binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( (!\binary_in[2]~input_o\ & !\binary_in[3]~input_o\) ) ) ) # ( \binary_in[0]~input_o\ & ( 
-- !\binary_in[1]~input_o\ & ( !\binary_in[2]~input_o\ $ (\binary_in[3]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0000000000000000101001011010010110100000101000001111000011110000",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_binary_in[2]~input_o\,
	datac => \ALT_INV_binary_in[3]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux1~0_combout\);

-- Location: LABCELL_X1_Y19_N36
\Mux0~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \Mux0~0_combout\ = ( \binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ & ( (!\binary_in[2]~input_o\) # (\binary_in[3]~input_o\) ) ) ) # ( !\binary_in[0]~input_o\ & ( \binary_in[1]~input_o\ ) ) # ( \binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( 
-- (\binary_in[2]~input_o\) # (\binary_in[3]~input_o\) ) ) ) # ( !\binary_in[0]~input_o\ & ( !\binary_in[1]~input_o\ & ( !\binary_in[3]~input_o\ $ (!\binary_in[2]~input_o\) ) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011110000111100001111110011111111111111111111111111001111110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => \ALT_INV_binary_in[3]~input_o\,
	datac => \ALT_INV_binary_in[2]~input_o\,
	datae => \ALT_INV_binary_in[0]~input_o\,
	dataf => \ALT_INV_binary_in[1]~input_o\,
	combout => \Mux0~0_combout\);

-- Location: LABCELL_X19_Y10_N0
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


