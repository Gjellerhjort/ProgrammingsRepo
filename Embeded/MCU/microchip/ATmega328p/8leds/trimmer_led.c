#define F_CPU 16000000UL
#define BAUD 9600
#define ADCW _SFR_MEM16(0x78)
#include <avr/io.h>
#include <util/delay.h>
#include <util/setbaud.h>

void UART_Init()
{
    UBRR0H = UBRRH_VALUE;
    UBRR0L = UBRRL_VALUE;
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    UCSR0C = (3 << UCSZ00);
}

void UART_Transmit(unsigned char data)
{
    while (!(UCSR0A & (1 << UDRE0)));
    UDR0 = data;
}

int main(void)
{
    UART_Init();
    DDRB = 0xFF;         // Alle pinne på PORTB er Output
    DDRD = 0xFF;         // Alle pinne på PORTD er Output
    ADCSRA = 0b10000111; // Aktiver ADC og del systemclock med 128
    ADMUX = 0b01000000;  // 2,56V Vref valgt. ADC arbejder ifht. 0V
    while (1)
    {

        ADCSRA |= (1 << ADSC); // Start analog konvertering
        while ((ADCSRA & (1 << ADIF)) == 0)
            ; // Vent på at konverteringen er afsluttet
        UART_Transmit(ADCW);
        UART_Transmit(0x0a);
        _delay_ms(100);
        if ((ADCW > 0) & (ADCW < 10)) // Læser HELE indholdet af ADC konverteringen
            PORTD = 0;
        if (ADCW >= 102) // over 0,5V
            PORTD = 0x01;
        if (ADCW >= 204) // over 1,0V
            PORTD = 0x03;
        if (ADCW >= 306) // over 1,5V
            PORTD = 0x07;
        if (ADCW >= 408) // over 2,0V
            PORTD = 0x0F;
        if (ADCW >= 510) // over 2,5V
            PORTD = 0x1F;
        if (ADCW >= 612) // over 3,0V
            PORTD = 0x3F;
        if (ADCW >= 714) // over 3,5V
            PORTD = 0x7F;
        if (ADCW >= 816) // over 4,0V
        {
            PORTD = 0xFF;
            PORTB = 0;
        }
        if (ADCW >= 918) // over 4,5V
        {
            PORTD = 0xFF;
            PORTB = 0x01;
        }
        if (ADCW >= 1020) // over 4,98V
        {
            PORTD = 0xFF;
            PORTB = 0x03;
        }
    }
    return 0;
}