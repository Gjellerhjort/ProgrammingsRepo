/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8
**/
#define F_CPU 16000000UL
#define delay 100
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    DDRD |= 0xFF;
    DDRB |= 0b000000111;
    while (1)
    {
        for (int x = 0; x <= 8; x++)
        {
            PORTD &= ~(1 << x - 2);
            PORTD |= (1 << x);
            // registerWrite(PORTD);
            _delay_ms(delay);
        }
        for (int x = 6; x >= 0; x--)
        {
            PORTD &= ~(1 << x + 2);
            PORTD |= (1 << x);
            // registerWrite(PORTD);
            _delay_ms(delay);
        }
    }
}
