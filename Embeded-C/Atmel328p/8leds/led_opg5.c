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
    int z = 8;
    while (1)
    {
        for (int x = 0; x < z ; x++)
        {
            PORTD &= ~(1 << x - 1);
            PORTD |= (1 << x);
            if (x >= z-1)
            {
                x = 0;
                z -= 1;
            }
            _delay_ms(delay);
            if (PORTD >= 0xFF)
            {
                z = 8;
                PORTD == 0x00;
            }
            //registerWrite(PORTD);

        }
    }
}
