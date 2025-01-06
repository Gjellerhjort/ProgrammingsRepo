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

-- DATE "01/06/2025 16:15:21"

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

ENTITY 	test1 IS
    PORT (
	switch0 : IN std_logic;
	switch1 : IN std_logic;
	switch2 : IN std_logic;
	switch3 : IN std_logic;
	led0 : BUFFER std_logic
	);
END test1;

-- Design Ports Information
-- led0	=>  Location: PIN_AA2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- switch0	=>  Location: PIN_E2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- switch1	=>  Location: PIN_L2,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- switch2	=>  Location: PIN_L1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- switch3	=>  Location: PIN_D3,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF test1 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_switch0 : std_logic;
SIGNAL ww_switch1 : std_logic;
SIGNAL ww_switch2 : std_logic;
SIGNAL ww_switch3 : std_logic;
SIGNAL ww_led0 : std_logic;
SIGNAL \~QUARTUS_CREATED_GND~I_combout\ : std_logic;
SIGNAL \switch2~input_o\ : std_logic;
SIGNAL \switch1~input_o\ : std_logic;
SIGNAL \switch3~input_o\ : std_logic;
SIGNAL \switch0~input_o\ : std_logic;
SIGNAL \led0~0_combout\ : std_logic;
SIGNAL \ALT_INV_switch3~input_o\ : std_logic;
SIGNAL \ALT_INV_switch2~input_o\ : std_logic;
SIGNAL \ALT_INV_switch1~input_o\ : std_logic;
SIGNAL \ALT_INV_switch0~input_o\ : std_logic;

BEGIN

ww_switch0 <= switch0;
ww_switch1 <= switch1;
ww_switch2 <= switch2;
ww_switch3 <= switch3;
led0 <= ww_led0;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;
\ALT_INV_switch3~input_o\ <= NOT \switch3~input_o\;
\ALT_INV_switch2~input_o\ <= NOT \switch2~input_o\;
\ALT_INV_switch1~input_o\ <= NOT \switch1~input_o\;
\ALT_INV_switch0~input_o\ <= NOT \switch0~input_o\;

-- Location: IOOBUF_X0_Y18_N79
\led0~output\ : cyclonev_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false",
	shift_series_termination_control => "false")
-- pragma translate_on
PORT MAP (
	i => \led0~0_combout\,
	devoe => ww_devoe,
	o => ww_led0);

-- Location: IOIBUF_X0_Y20_N55
\switch2~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_switch2,
	o => \switch2~input_o\);

-- Location: IOIBUF_X0_Y20_N38
\switch1~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_switch1,
	o => \switch1~input_o\);

-- Location: IOIBUF_X0_Y20_N4
\switch3~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_switch3,
	o => \switch3~input_o\);

-- Location: IOIBUF_X0_Y20_N21
\switch0~input\ : cyclonev_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_switch0,
	o => \switch0~input_o\);

-- Location: LABCELL_X1_Y20_N0
\led0~0\ : cyclonev_lcell_comb
-- Equation(s):
-- \led0~0_combout\ = ( \switch0~input_o\ & ( (!\switch2~input_o\) # ((!\switch3~input_o\) # (\switch1~input_o\)) ) ) # ( !\switch0~input_o\ & ( (!\switch2~input_o\) # (!\switch3~input_o\) ) )

-- pragma translate_off
GENERIC MAP (
	extended_lut => "off",
	lut_mask => "1111101011111010111110111111101111111010111110101111101111111011",
	shared_arith => "off")
-- pragma translate_on
PORT MAP (
	dataa => \ALT_INV_switch2~input_o\,
	datab => \ALT_INV_switch1~input_o\,
	datac => \ALT_INV_switch3~input_o\,
	datae => \ALT_INV_switch0~input_o\,
	combout => \led0~0_combout\);

-- Location: LABCELL_X5_Y9_N3
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


