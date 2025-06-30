CC = arm-none-eabi-gcc
AS = arm-none-eabi-as
LD = arm-none-eabi-ld
OBJCOPY = arm-none-eabi-objcopy
STLINK = st-flash

CFLAGS = -mthumb -mcpu=cortex-m3

all: app.bin

crt.o: crt.s
	$(AS) $(CFLAGS) -o $@ $<

main.o: main.c
	$(CC) $(CFLAGS) -c -o $@ $<

app.elf: crt.o main.o linker.ld
	$(LD) -T linker.ld -o $@ crt.o main.o

app.bin: app.elf
	$(OBJCOPY) -O binary app.elf $@

flash: app.bin
	$(STLINK) write app.bin 0x08000000

clean:
	rm -f *.o *.elf *.bin
