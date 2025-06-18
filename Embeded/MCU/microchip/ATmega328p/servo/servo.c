#define F_CPU 12000000UL

#include <avr/io.h>
#include <util/delay.h>

long map(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void servoTurn(int deg)
{
    OCR1A = map(deg,0,180,2000,4000);
}

int main(void)
{
    DDRB |= 1 << PINB1;

    TCCR1A |= (1 << WGM11) | (1 << COM1A1);
    // CS11 sætter clock division til 8
    
    TCCR1B |= (1 << WGM12) | (1 << WGM13) | (1 << CS11);
    // WGM sætter timeren til CTC mode

    // Timer/Counter1 - Input Capture Register
    ICR1 = 39999;

    int offset = 520;

    while(1)    
    {
        // 65535
        // compare match værdi
        servoTurn(0);
        _delay_ms(4000);
        servoTurn(180);

        _delay_ms(4000);
    }
    return 0;
}