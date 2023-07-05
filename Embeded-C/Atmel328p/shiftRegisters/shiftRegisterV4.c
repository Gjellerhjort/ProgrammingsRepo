/**
Latchpin(yellow) = 10
Clockpin(white) = 9
DataPin(green) = 8
**/
#define F_CPU 16000000UL
#define delay 100
#include <avr/io.h>
#include <util/delay.h>
int oldvalue;

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

long map(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

int main(void)
{
    DDRB |= 0b000000111;
    ADCSRA = 0b10000111; // Aktiver ADC og del systemclock med 128
    ADMUX = 0b01000000;  // 5V Vref valgt. ADC arbejder ifht. 0V
    while (1)
    {
        ADCSRA |= (1 << ADSC);
        // Start analog konvertering
        while ((ADCSRA & (1 << ADIF)) == 0); // Vent på at konverteringen er afsluttet
        int value = map(ADCW, 0, 1024, 0, 8); // maps the value from the ADCW fro 0,1024 to 0,8. 
        if (value != oldvalue) // removes noise in shiftregister 
        {
            registerWrite((1<<value));
            oldvalue = value;
        }

    }
}

