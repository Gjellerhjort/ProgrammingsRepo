#define PERIPH_BASE     0x40000000
#define APB2PERIPH_BASE (PERIPH_BASE + 0x10000)
#define AHBPERIPH_BASE  (PERIPH_BASE + 0x20000)

#define RCC_BASE        (AHBPERIPH_BASE + 0x1000)
#define GPIOC_BASE      (APB2PERIPH_BASE + 0x1000)

#define RCC_APB2ENR     (*(volatile unsigned int*)(RCC_BASE + 0x18))
#define GPIOC_CRH       (*(volatile unsigned int*)(GPIOC_BASE + 0x04))
#define GPIOC_ODR       (*(volatile unsigned int*)(GPIOC_BASE + 0x0C))

#define RCC_IOPCEN      (1 << 4)

void delay(volatile int time) {
    while (time--);
}

int main(void) {
    // Enable GPIOC clock
    RCC_APB2ENR |= RCC_IOPCEN;

    // Configure PC13 as push-pull output
    GPIOC_CRH &= ~(0xF << 20);     // Clear CNF and MODE bits
    GPIOC_CRH |=  (0x1 << 20);     // MODE = 01 (output 10 MHz)
                                   // CNF = 00 (general push-pull)

    while (1) {
        GPIOC_ODR ^= (1 << 13);    // Toggle PC13
        delay(500000);
    }

    return 0;
}
