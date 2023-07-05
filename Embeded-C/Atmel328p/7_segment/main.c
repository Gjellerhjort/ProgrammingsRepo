#define F_CPU 16000000UL
#define KORT_PAUSE _delay_ms(500)
#define PAUSE _delay_ms(2000)
#include <avr/io.h>
#include <util/delay.h>
#include "7segment.h"
int main()
{
unsigned char i,j;
// Test af "init7segmentport"
init7segmentport();
_delay_ms(2000);
// Test af Segment
turnOnAllSegments();
_delay_ms(2000);
turnOffAllSegments();
_delay_ms(2000);
// Test1 af "Skrivtal"
for (j=0; j<10;j++)
{
for (i=0; i<6; i++)
{
PORTD = 1<<i;
_delay_ms(200);
}
}
turnOffAllSegments();
_delay_ms(2000);
// Test2 af "Skrivtal"
for (i=0; i<=9; i++)
{
writeNumber(i);
_delay_ms(2000);
}
// Bliv her
while (1)
{}
return 0;
}