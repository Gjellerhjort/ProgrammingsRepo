/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8
**/
#define F_CPU 16000000UL
#define delay 100
#include <avr/io.h>
#include <util/delay.h>

void registerWrite(unsigned char inputByte)
{
    for (int i = 0; i <= 8; i++)
    {
        if (inputByte & (1 << i))
        {
            PORTB = 0b000000011;
            PORTB = 0b000000100; // write data to output when latchpin is high
        }
        else
        {
            PORTB = 0b000000010;
            PORTB = 0b000000100; // write data to output when latchpin is high
        }
    }
}

int main(void)
{
    DDRB |= 0b000000111;
    unsigned char ShiftRegister = 0;
    while (1)
    {
        for (int x = 1; x <= 7; x++)
        {
            ShiftRegister &= ~(1 << x - 1);
            ShiftRegister |= (1 << x);

            registerWrite(ShiftRegister);
            _delay_ms(delay);
        }
        for (int x = 6; x >= 0; x--)
        {
            ShiftRegister &= ~(1 << x + 1);
            ShiftRegister |= (1 << x);

            registerWrite(ShiftRegister);
            _delay_ms(delay);
        }
    }
}
