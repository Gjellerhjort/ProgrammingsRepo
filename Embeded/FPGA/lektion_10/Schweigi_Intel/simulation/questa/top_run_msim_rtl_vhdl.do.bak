transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_10/Schweigi_Intel/top_w_proc_2.vhd}
vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_10/Schweigi_Intel/hs_uart.vhd}
vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_10/Schweigi_Intel/bytetx.vhd}
vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_10/Schweigi_Intel/ALU.vhd}

vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_10/Schweigi_Intel/top_w_proc_2_tb.vhd}

vsim -t 1ps -L altera -L lpm -L sgate -L altera_mf -L altera_lnsim -L cyclonev -L cyclonev_hssi -L rtl_work -L work -voptargs="+acc"  top_w_proc_2_tb

add wave *
view structure
view signals
run -all
