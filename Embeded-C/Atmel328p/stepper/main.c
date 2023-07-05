#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>
// Set baud rate
#define BAUD 9600
#define UBRR_VAL ((F_CPU / (BAUD * 16UL)) - 1)

#define RX_BUFFER_SIZE 10
#define TX_BUFFER_SIZE 10
// Receive buffer
char rx_buffer[RX_BUFFER_SIZE];
volatile uint8_t rx_index = 0;

// Transmit buffer
char tx_buffer[TX_BUFFER_SIZE];
volatile uint8_t tx_index = 0;
volatile uint8_t tx_count = 0;

// Initialize UART
void uart_init() {
    // Set baud rate
    UBRR0H = (uint8_t)(UBRR_VAL >> 8);
    UBRR0L = (uint8_t)(UBRR_VAL);
    // Enable receiver and transmitter
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);
    // Set frame format: 8 data bits, 1 stop bit
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
    // Enable RX complete interrupt
    UCSR0B |= (1 << RXCIE0);
}

// Send a single character
void uart_putc(char data) {
    // Wait for empty transmit buffer
    while (!(UCSR0A & (1 << UDRE0)));
    // Put data into buffer, sends the data
    UDR0 = data;
}

// Send a string
void uart_puts(char* str) {
    while (*str) {
        uart_putc(*str++);
    }
}

// Receive a single character
char uart_getc() {
    // Wait for data to be received
    while (!(UCSR0A & (1 << RXC0)));
    // Get and return received data from buffer
    return UDR0;
}

void step()
{
    PORTD = 0b00001100;
    _delay_ms(1000);
    PORTD = 0b00011000;
    _delay_ms(1000);
    PORTD = 0b00110000;
    _delay_ms(1000);
    PORTD = 0b00100100;
    _delay_ms(1000);
}

void rotateLeft()
{
    PORTD = 0b00010000;
    _delay_ms(1.2);
    PORTD = 0b00100000;
    _delay_ms(1.2);
    PORTD = 0b01000000;
    _delay_ms(1.2);
    PORTD = 0b10000000;
    _delay_ms(1.2);
}

void rotateRight()
{
    PORTD = 0b10000000;
    _delay_ms(1.2);
    PORTD = 0b01000000;
    _delay_ms(1.2);
    PORTD = 0b00100000;
    _delay_ms(1.2);
    PORTD = 0b00010000;
    _delay_ms(1.2);
}

// Interrupt service routine for receive complete interrupt
ISR(USART_RX_vect) {
    char data = UDR0;
    if (rx_index < RX_BUFFER_SIZE) {
        rx_buffer[rx_index++] = data;
    }
}

// Interrupt service routine for transmit complete interrupt
ISR(USART_TX_vect) {
    if (tx_count > 0) {
        UDR0 = tx_buffer[tx_index++];
        if (tx_index >= TX_BUFFER_SIZE) {
            tx_index = 0;
        }
        tx_count--;
    }
}

int main()
{
    DDRD = 0xff;
    uart_init();
    sei(); // Enable global interrupts
    char string[10];
    while (1)
    {
        for (int x=0; x<400; x++)
        {
            itoa(x , string, 10);
            uart_puts(string);
            rotateLeft();
        }
        _delay_ms(1000);
        for (int x=0; x<400; x++)
        {
            rotateRight();
        }

    }
    return 0;
}