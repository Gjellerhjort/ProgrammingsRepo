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
    while (1)
    {
        for (int x = 0; x <= 8; x++)
        {
            PORTD = (1<<x);
            //registerWrite(ShiftRegister);
            _delay_ms(delay);
        }
    }
}
