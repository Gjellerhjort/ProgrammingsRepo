#include <avr/io.h>
#include <avr/iterrupt.h>

#define STEPPER_PIN_1 PB2
#define STEPPER_PIN_2 PB3
#define STEPPER_PIN_3 PB4
#define STEPPER_PIN_4 PB5

long map(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void Forward()
{   
    while()
    PORTD = 0b00001000;
    _delay_ms(4);
    PORTD = 0b00100000;
    _delay_ms(4);
    PORTD = 0b00000100;
    _delay_ms(4);
    PORTD = 0b01000000;
    _delay_ms(4);
}

void StepRottate(int speed)
{

}