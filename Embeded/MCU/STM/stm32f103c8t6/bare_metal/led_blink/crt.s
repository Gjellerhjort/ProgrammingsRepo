.cpu cortex-m3
.thumb

    .word 0x20005000     // initial stack pointer (end of 20 KB RAM)
    .word _reset         // reset handler address

.thumb_func
_reset:
    bl main
    b .

