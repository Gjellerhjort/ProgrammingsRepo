#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
DDRB |= 0b000100000;
DDRC &= 0;
while (1)
{
    PORTB = 0b000100000;
    _delay_ms(300);
    PORTB &= 0b000000000;
    _delay_ms(300);
}
return 0;
}


