#define F_CPU 16000000UL
#define BAUD 9600 
#include <avr/io.h>
#include <util/delay.h>
#include<util/setbaud.h>    

void UART_Init()
{
   UBRR0H = UBRRH_VALUE;
   UBRR0L = UBRRL_VALUE; 
   UCSR0B = (1<<RXEN0) | (1<<TXEN0);
   UCSR0C = (3<<UCSZ00);
}

void UART_Transmit(unsigned char data)
{
    while(!(UCSR0A & (1<<UDRE0)));
    UDR0 = data;
}

int main(void)
{
UART_Init();
DDRB |= 0b00001111;
DDRC &= 0;
while (1)
{
    PORTB = PINC;
    UART_Transmit(PINC);
}
return 0;
}
