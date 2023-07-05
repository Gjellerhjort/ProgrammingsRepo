#include <avr/io.h>

#define number_Count 10

char segmentNumber[number_Count] = {
    0b01111110,              // 0
    0b00110000,              // 1
    0b01011011,              // 2
    0b01001111,              // 3
    0b00110011,              // 4
    0b01011011,              // 5
    0b01011111,              // 6
    0b01110000,              // 7
    0b01111111,              // 8
    0b01100111               // 9
};

void init7segmentport() 
{
    DDRD = 0xff;
    DDRB = 0xff;
    PORTD = 0xff;
    PORTB = 0x00;
}
void turnOnAllSegments() 
{
    PORTD = 0x00;
}
void turnOffAllSegments()
{
    PORTD = 0xff;
}
void writeNumber(int number, int segment_Number) 
{
    switch (segment_Number) {
        case 1:
            PORTB = 0x01;
            PORTD = ~segmentNumber[number];

          break;
    
        case 2:
            PORTB = 0x02;
            PORTD = ~segmentNumber[number];
          break;
          
        default:
            break;
    }

}