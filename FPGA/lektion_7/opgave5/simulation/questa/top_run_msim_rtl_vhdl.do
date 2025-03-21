transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_7/opgave5/adder4.vhd}
vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_7/opgave5/adder.vhd}

vcom -93 -work work {/home/user/Github/ProgrammingsRepo/FPGA/lektion_7/opgave5/adder4_tb.vhd}

vsim -t 1ps -L altera -L lpm -L sgate -L altera_mf -L altera_lnsim -L cyclonev -L cyclonev_hssi -L rtl_work -L work -voptargs="+acc"  adder4_tb

add wave *
view structure
view signals
run -all
