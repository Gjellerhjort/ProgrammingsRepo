.syntax unified
.cpu cortex-m3
.thumb

.global Reset_Handler
.global _estack

.section .isr_vector, "a", %progbits
.type isr_vector, %object
.size isr_vector, .-isr_vector
isr_vector:
  .word _estack
  .word Reset_Handler

.section .text
Reset_Handler:
  ldr r0, =_sbss
  ldr r1, =_ebss
  movs r2, #0
  bss_loop:
    cmp r0, r1
    it lt
    strlt r2, [r0], #4
    blt bss_loop

  ldr r0, =_sdata
  ldr r1, =_etext
  ldr r2, =_edata
  copy_data:
    cmp r0, r2
    it lt
    ldrlt r3, [r1], #4
    strlt r3, [r0], #4
    blt copy_data

  bl main
  b .
.size Reset_Handler, .-Reset_Handler

.section .stack
.space 0x1000
_estack:
