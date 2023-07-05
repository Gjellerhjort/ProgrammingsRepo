/*
 * _7segment.S
 *
 * Created: 19-01-2023 08:42:18
 *  Author: lauri
 */ 
#define F_CPU 16000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include "7segment.h"
int timecount = 0;
int count = 0;

void initTimer() 
{
    //DDRB = 0x01; // Arduino bit 8 benyttes
	TCCR0A = (1 << WGM01); //Aktiver CTC Bit
	OCR0A = 61; // Se https://eleccelerator.com/avr-timer-calculator/
	TIMSK0 = (1 << OCIE0A); //Generer interrupt, når OCR0A værdi nås
	sei(); // Set External Interrupt
	// Aktiverer I-bit i status registeret
	TCCR0B = (1 << CS02) | (0 << CS00); // Benyt prescalar på 1024
}


void main() 
{
    init7segmentport();
    initTimer();
	while(1)
	{
        if (count>=100)
        {
            count = 0;
        }
	   writeNumber((count%10), 1);
	   writeNumber((count/10), 2);  
	}
}

ISR(TIMER0_COMPA_vect)
{
	timecount++;
	if(timecount >= 1000)
	{
		count++;
		timecount = 0;		  
	}
}