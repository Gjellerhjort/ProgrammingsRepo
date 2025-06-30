#include <stdint.h>

// Registers for RCC and GPIOC
#define RCC_APB2ENR (*(volatile uint32_t*)0x40021018)
#define GPIOC_CRH   (*(volatile uint32_t*)0x40011004)
#define GPIOC_ODR   (*(volatile uint32_t*)0x4001100C)

#define RCC_IOPCEN  (1 << 4)
#define GPIOC13     (1 << 13)

void main(void) {
    // Enable clock for GPIOC
    RCC_APB2ENR |= RCC_IOPCEN;

    // Configure PC13 as push-pull output (2 MHz)
    GPIOC_CRH &= 0xFF0FFFFF;
    GPIOC_CRH |= 0x00200000;

    // Blink loop
    while (1) {
        GPIOC_ODR &= ~GPIOC13;  // LED on (PC13 LED is active low)
        for (volatile int i = 0; i < 5000000; i++);
        GPIOC_ODR |= GPIOC13;   // LED off
        for (volatile int i = 0; i < 5000000; i++);
    }
}
