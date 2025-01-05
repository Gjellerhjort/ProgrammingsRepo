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

-- DATE "01/04/2025 23:17:55"

-- 
-- Device: Altera 5CEBA4F23C7 Package FBGA484
-- 

-- 
-- This VHDL file should be used for Questa Intel FPGA (VHDL) only
-- 

LIBRARY ALTERA;
LIBRARY ALTERA_LNSIM;
LIBRARY CYCLONEV;
LIBRARY IEEE;
USE ALTERA.ALTERA_PRIMITIVES_COMPONENTS.ALL;
USE ALTERA_LNSIM.ALTERA_LNSIM_COMPONENTS.ALL;
USE CYCLONEV.CYCLONEV_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY 	shiftRegister1 IS
    PORT (
	btn : IN std_logic;
	swtch : IN std_logic;
	LED : BUFFER std_logic_vector(3 DOWNTO 0)
	);
END shiftRegister1;

-- Design Ports Information
-- LED[0]	=>  Location: PIN_N1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- LED[1]	=>  Location: PIN_N2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- LED[2]	=>  Location: PIN_U2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- LED[3]	=>  Location: PIN_U1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- btn	=>  Location: PIN_M16,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- swtch	=>  Location: PIN_D3,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF shiftRegister1 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_btn : std_logic;
SIGNAL ww_swtch : std_logic;
SIGNAL ww_LED : std_logic_vector(3 DOWNTO 0);
SIGNAL \~QUARTUS_CREATED_GND~I_combout\ : std_logic;
SIGNAL \btn~input_o\ : std_logic;
SIGNAL \btn~inputCLKENA0_outclk\ : std_logic;
SIGNAL \swtch~input_o\ : std_logic;
SIGNAL \LED[0]~reg0feeder_combout\ : std_logic;
SIGNAL \LED[0]~reg0_q\ : std_logic;
SIGNAL \buff[1]~feeder_combout\ : std_logic;
SIGNAL \LED[1]~reg0_q\ : std_logic;
SIGNAL \LED[2]~reg0feeder_combout\ : std_logic;
SIGNAL \LED[2]~reg0_q\ : std_logic;
SIGNAL \buff[3]~feeder_combout\ : std_logic;
SIGNAL \LED[3]~reg0_q\ : std_logic;
SIGNAL buff : std_logic_vector(3 DOWNTO 0);
SIGNAL \ALT_INV_btn~inputCLKENA0_outclk\ : std_logic;
SIGNAL ALT_INV_buff : std_logic_vector(2 DOWNTO 0);

BEGIN

ww_btn <= btn;
ww_swtch <= swtch;
LED <= ww_LED;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_btn~inputCLKENA0_outclk\ <= NOT \btn~inputCLKENA0_outclk\;
ALT_INV_buff(2) <= NOT buff(2);
ALT_INV_buff(0) <= NOT buff(0);

-- Location: IOOBUF_X0_Y19_N56
\LED[0]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \LED[0]~reg0_q\,
	devoe => ww_devoe,
	o => ww_LED(0));

-- Location: IOOBUF_X0_Y19_N39
\LED[1]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \LED[1]~reg0_q\,
	devoe => ww_devoe,
	o => ww_LED(1));

-- Location: IOOBUF_X0_Y19_N5
\LED[2]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \LED[2]~reg0_q\,
	devoe => ww_devoe,
	o => ww_LED(2));

-- Location: IOOBUF_X0_Y19_N22
\LED[3]~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \LED[3]~reg0_q\,
	devoe => ww_devoe,
	o => ww_LED(3));

-- Location: IOIBUF_X54_Y18_N61
\btn~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_btn,
	o => \btn~input_o\);

-- Location: CLKCTRL_G10
\btn~inputCLKENA0\ : cyclonev_clkena
-- pragma translate_off
GENERIC MAP (
	clock_type => "global clock",
	disable_mode => "low",
	ena_register_mode => "always enabled",
	ena_register_power_up => "high",
	test_syn => "high")
-- pragma translate_on
PORT MAP (
	inclk => \btn~input_o\,
	outclk => \btn~inputCLKENA0_outclk\);

-- Location: IOIBUF_X0_Y20_N4
\swtch~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_swtch,
	o => \swtch~input_o\);

-- Location: FF_X1_Y19_N14
\buff[0]\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	asdata => \swtch~input_o\,
	sload => VCC,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => buff(0));

-- Location: LABCELL_X1_Y19_N45
\LED[0]~reg0feeder\ : cyclonev_lcell_comb
-- Equation(s):
-- \LED[0]~reg0feeder_combout\ = buff(0)

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011001100110011001100110011001100110011001100110011001100110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => ALT_INV_buff(0),
	combout => \LED[0]~reg0feeder_combout\);

-- Location: FF_X1_Y19_N47
\LED[0]~reg0\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	d => \LED[0]~reg0feeder_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => \LED[0]~reg0_q\);

-- Location: LABCELL_X1_Y19_N33
\buff[1]~feeder\ : cyclonev_lcell_comb
-- Equation(s):
-- \buff[1]~feeder_combout\ = buff(0)

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011001100110011001100110011001100110011001100110011001100110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => ALT_INV_buff(0),
	combout => \buff[1]~feeder_combout\);

-- Location: FF_X1_Y19_N35
\buff[1]\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	d => \buff[1]~feeder_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => buff(1));

-- Location: FF_X1_Y19_N31
\LED[1]~reg0\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	asdata => buff(1),
	sload => VCC,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => \LED[1]~reg0_q\);

-- Location: FF_X1_Y19_N44
\buff[2]\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	asdata => buff(1),
	sload => VCC,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => buff(2));

-- Location: LABCELL_X1_Y19_N54
\LED[2]~reg0feeder\ : cyclonev_lcell_comb
-- Equation(s):
-- \LED[2]~reg0feeder_combout\ = buff(2)

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011001100110011001100110011001100110011001100110011001100110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => ALT_INV_buff(2),
	combout => \LED[2]~reg0feeder_combout\);

-- Location: FF_X1_Y19_N56
\LED[2]~reg0\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	d => \LED[2]~reg0feeder_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => \LED[2]~reg0_q\);

-- Location: LABCELL_X1_Y19_N57
\buff[3]~feeder\ : cyclonev_lcell_comb
-- Equation(s):
-- \buff[3]~feeder_combout\ = buff(2)

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "0011001100110011001100110011001100110011001100110011001100110011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	datab => ALT_INV_buff(2),
	combout => \buff[3]~feeder_combout\);

-- Location: FF_X1_Y19_N59
\buff[3]\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	d => \buff[3]~feeder_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => buff(3));

-- Location: FF_X1_Y19_N16
\LED[3]~reg0\ : dffeas
-- pragma translate_off
GENERIC MAP (
	is_wysiwyg => "true",
	power_up => "low")
-- pragma translate_on
PORT MAP (
	clk => \ALT_INV_btn~inputCLKENA0_outclk\,
	asdata => buff(3),
	sload => VCC,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	q => \LED[3]~reg0_q\);

-- Location: LABCELL_X50_Y10_N3
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


