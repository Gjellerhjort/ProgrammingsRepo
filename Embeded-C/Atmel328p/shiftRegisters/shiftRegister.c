#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8

**/


int main(void)
{
DDRB |= 0b000000111;
while (1)
{
    PORTB = 0b000000011; //writes 1 to data and clocks it so it puts a 0 in the shift register
    PORTB = 0b000000100; //write data to output when latchpin is high
    _delay_ms(100);
    PORTB = 0b000000010; //writes 0 to data and clocks it so it puts a 0 in the shift register
    PORTB = 0b000000100;//write data to output when latchpin is high
    _delay_ms(100); 
}
return 0;
}


