CC=arm-none-eabi-gcc
CFLAGS=-mcpu=cortex-m3 -mthumb -Os -Wall
LDFLAGS=-Tstm32f103.ld -nostartfiles

all: main.elf

main.elf: main.o startup.o
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

main.o: main.c
	$(CC) $(CFLAGS) -c $< -o $@

startup.o: startup.s
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o *.elf
