#define F_CPU 16000000UL
#define BAUD 9600
#include <util/delay.h>
#include <avr/io.h>
#include <util/setbaud.h>
#include <stdlib.h>
#include <string.h>
// Standard AVR headerfil
int led;
int pinNr = 0;
#define LED_COUNT 15
#define DDR_BYTE 0
#define PORT_BYTE 1

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
void SerialWrite(char data[10])
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
// Antal tilsluttede LEDs
char charlie[LED_COUNT][2] = {
    // DDR_BYTE PORT_BYTE        
    //ABCDE
    {0b00000000, 0b00000000}, // Alt slukket
    {0b00000011, 0b00000001},              // AB 1
    {0b00000011, 0b00000010},              // BA 2
    {0b00000110, 0b00000010},              // BC 3
    {0b00000110, 0b00000100},              // CB 4
    {0b00001100, 0b00000100},              // AC 5
    {0b00001100, 0b00001000},              // CA 6
    {0b00000101, 0b00000001},              // AD 7
    {0b00000101, 0b00000100},              // DA 8
    {0b00001010, 0b00000010},              // BD 9
    {0b00001010, 0b00001000},              // DB 10
    {0b00001001, 0b0    0000001},              // CD 11
    {0b00001001, 0b00001000},              // DC 12
    {0b00010001, 0b00000001},               // DE 13
    {0b00010001, 0b00010000},               // DE 14
};
void turnOn(char led)
{
    // Styring af Charlieplexing LEDs
    DDRB = charlie[led][DDR_BYTE];
    PORTB = charlie[led][PORT_BYTE];
}
int laesKnapper()
{
    if (ADCW > 80 && ADCW < 140)
        pinNr = 2;
    else if (ADCW >= 200 && ADCW < 280)
        pinNr = 3;
    else if (ADCW >= 290 && ADCW < 330)
        pinNr = 4;
    else if (ADCW >= 340 && ADCW < 380)
        pinNr = 5;
    else if (ADCW >= 400 && ADCW < 440)
        pinNr = 6;
    else if (ADCW >= 450 && ADCW < 490)
        pinNr = 7;
    else if (ADCW >= 530 && ADCW < 570)
        pinNr = 8;
    else if (ADCW >= 580 && ADCW < 610)
        pinNr = 9;
    else if (ADCW >= 620 && ADCW < 670)
        pinNr = 10;
    else if (ADCW >= 680 && ADCW < 730)
        pinNr = 11;
    else if (ADCW   >= 750 && ADCW < 830)
        pinNr = 12;
    else if (ADCW >= 850 && ADCW < 950)
        pinNr = 13;
    else if (ADCW >= 980 && ADCW < 1030)
        pinNr = 14;
    else
        pinNr = 0;
    return (pinNr);
}
int main(void)
{
    char string[10] = "";
    UART_Init();
    ADCSRA = 0b10000111; // Aktiver ADC og del systemclock med 128
    ADMUX = 0b01000000;  // 5V Vref valgt. ADC arbejder ifht. 0V
    while (1)
    {
        //for (int x=1; x<15; x++) 
        //{
        //    turnOn(x);
        //    _delay_ms(100);
        //}
        ADCSRA |= (1 << ADSC);
        // Start analog konvertering
        while ((ADCSRA & (1 << ADIF)) == 0); // Vent på at konverteringen er afsluttet
        
        itoa(ADCW, string, 10);
        SerialWrite(string);
        if (ADCW > 80 && ADCW < 1030)
        {
            pinNr = laesKnapper();
            turnOn(pinNr);
        }
        else
            turnOn(1);
        
    }
    return 0;
}