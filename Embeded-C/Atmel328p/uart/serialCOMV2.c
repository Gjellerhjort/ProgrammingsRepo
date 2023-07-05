#define F_CPU 16000000UL
#define BAUD 9600
#include <avr/io.h>
#include <util/delay.h>
#include <util/setbaud.h>
#include <stdlib.h>
#include <string.h>

void UART_Init()
{
    UBRR0H = UBRRH_VALUE;
    UBRR0L = UBRRL_VALUE;
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    UCSR0C = (3 << UCSZ00);
}

void UART_Transmit(unsigned char data)
{
    while (!(UCSR0A & (1 << UDRE0)))
        ;
    UDR0 = data;
}

void SerialWrite(char data[20])
{
    int i = 0;
    while (data[i] != '\0')
    { // takes every charters in the string and sends it
        UART_Transmit(data[i]);
        i++;
    }
    UART_Transmit(0x0a); // newline
    UART_Transmit(0x0d); // sets cursor left
}

int main(void)
{
    char string[20] = "";
    UART_Init();
    ADCSRA = 0b10000111; // Aktiver ADC og del systemclock med 128
    ADMUX = 0b01000000;  // 5V Vref valgt. ADC arbejder ifht. 0V
    while (1)
    {
        ADCSRA |= (1 << ADSC);
        // Start analog konvertering
        while ((ADCSRA & (1 << ADIF)) == 0)
            ; // Vent på at konverteringen er afsluttet
        itoa(ADCW, string, 10);
        SerialWrite(string);
        _delay_ms(10);
    }
}