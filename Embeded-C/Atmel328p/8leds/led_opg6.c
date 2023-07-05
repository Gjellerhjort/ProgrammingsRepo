/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8
**/
#define F_CPU 16000000UL
#define delay 100
#include <avr/io.h>
#include <util/delay.h>

unsigned char ShiftRegister = 0;

void program1()
{
    for (int x = 0; x <= 8; x++)
    {
        ShiftRegister = (1 << x);
        PORTD = ShiftRegister;
        // registerWrite(ShiftRegister);
        _delay_ms(delay);
    }
}

void program2()
{
    for (int x = 1; x <= 7; x++)
    {
        ShiftRegister &= ~(1 << x - 2);
        ShiftRegister |= (1 << x);
        PORTD = ShiftRegister;
        // registerWrite(ShiftRegister);
        _delay_ms(delay);
    }
    for (int x = 6; x >= 0; x--)
    {
        ShiftRegister &= ~(1 << x + 2);
        ShiftRegister |= (1 << x);
        PORTD = ShiftRegister;
        // registerWrite(ShiftRegister);
        _delay_ms(delay);
    }
}

void program3()
{
    for (int x = 0; x <= 12; x++)
    {
        PORTD = (char)x;
        // registerWrite(x);
        _delay_ms(delay);
    }
}

void program4()
{
    for (int x = 1; x <= 7; x++)
    {
        ShiftRegister &= ~(1 << x - 1);
        ShiftRegister |= (1 << x);
        ShiftRegister &= ~(1 << 8 - x);
        ShiftRegister |= (1 << 7 - x);
        PORTD = ShiftRegister;
        // registerWrite(ShiftRegister);
        _delay_ms(delay);
    }
    for (int x = 6; x >= 0; x--)
    {
        ShiftRegister &= ~(1 << x + 1);
        ShiftRegister |= (1 << x);
        ShiftRegister &= ~(1 << 6 - x);
        ShiftRegister |= (1 << 7 - x);
        PORTD = ShiftRegister;
        // registerWrite(ShiftRegister);
        _delay_ms(delay);
    }
}

void state1()
{
    for (int x = 0; x < 2; x++)
    {
        program1();
    }
    for (int x = 0; x < 3; x++)
    {
        program2();
    }
    for (int x = 0; x < 4; x++)
    {
        program3();
    }
    for (int x = 0; x < 5; x++)
    {
        program4();
    }
}
void state2()
{
    for (int x = 0; x < 5; x++)
    {
        program1();
    }
    for (int x = 0; x < 4; x++)
    {
        program2();
    }
    for (int x = 0; x < 3; x++)
    {
        program3();
    }
    for (int x = 0; x < 2; x++)
    {
        program4();
    }
}

int main(void)
{
    DDRB &= 0;
    DDRD |= 0xFF;
    int program = 0;
    int z = 8;

    while (1)
    {
        if (PINB & (1 << 0))
        {
            program++;
            _delay_ms(200);
        }
        if (program > 2)
        {
            program = 0;
        }

        switch (program)
        {
        case 1:
            state1();
            break;
        case 2:
            state2();
        default:
            PORTD = 0xFF;
        break;
        }
    }
}
