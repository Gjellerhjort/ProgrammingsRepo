transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {C:/Users/ECC/Desktop/teaching/DD/Intel/Schweigi_Intel/top_w_proc_2.vhd}
vcom -93 -work work {C:/Users/ECC/Desktop/teaching/DD/Intel/Schweigi_Intel/hs_uart.vhd}
vcom -93 -work work {C:/Users/ECC/Desktop/teaching/DD/Intel/Schweigi_Intel/bytetx.vhd}
vcom -93 -work work {C:/Users/ECC/Desktop/teaching/DD/Intel/Schweigi_Intel/ALU.vhd}

