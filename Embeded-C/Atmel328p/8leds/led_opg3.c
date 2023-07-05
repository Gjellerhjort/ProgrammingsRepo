/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8
**/
#define F_CPU 16000000UL
#define delay 500
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    DDRD |= 0xFF;
    DDRB |= 0b000000111;
    while (1)
    {
        for (int x = 0; x <= 255; x++)
        {
            PORTD = x;
            //registerWrite(x);
            _delay_ms(delay);
        }
    }
}
