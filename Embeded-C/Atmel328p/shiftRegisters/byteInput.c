/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8
**/
#define F_CPU 16000000UL
#define delay 100
#include <avr/io.h>
#include <stdio.h>
#include <string.h>
#include <util/delay.h>

void registerWrite(char inputByte)
{
    for (int i = 0; i =< 8; i++)
    {   
        if (inputByte & (1<<i)) 
        {
            PORTB = 0b000000011;
            PORTB = 0b000000100; //write data to output when latchpin is high
        }
        else 
        {
            PORTB = 0b000000010;
            PORTB = 0b000000100; //write data to output when latchpin is high
        }
    }
}

int main(void)
{
DDRB |= 0b000000111;
    while (1)
    {
        registerWrite(0b10000000);
        _delay_ms(delay);
        registerWrite(0b01000000);
        _delay_ms(delay);
        registerWrite(0b00100000);
        _delay_ms(delay);
        registerWrite(0b00010000);
        _delay_ms(delay);
        registerWrite(0b00001000);
        _delay_ms(delay);
        registerWrite(0b00000100);
        _delay_ms(delay);
        registerWrite(0b00000010);
        _delay_ms(delay);
        registerWrite(0b00000001);
        _delay_ms(delay);
    }
}


