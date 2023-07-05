#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

char ipv4_address_class(const char *ipv4_addr)
{
    uint8_t  first_octet = atoi(ipv4_addr);
    if (!(first_octet & 0b10000000))
    {
        return 'A';
    }   else if (!(first_octet & 0b01000000))
    {
        return 'B';    
    }   else if (!(first_octet & 0b00100000))
    {
        return 'C';    
    }   else if (!(first_octet & 0b00010000))
    {
        return 'D';    
    } else if (!(first_octet & 0b00001000))
    {
        return 'E';    
    }
}

void should_be(const char *ipv4_addr, const char expected) {
  char result = ipv4_address_class(ipv4_addr);
  printf("IP: %s Expected: %c Returned: %c \n", ipv4_addr, expected,result);
}


int main(int argc, char const *argv[])
{
    // test function
    should_be("1.1.1.1",      'A');
    should_be("172.66.43.71", 'B');
    should_be("192.168.0.1",  'C');
    should_be("224.0.0.227",  'D');
    should_be("242.0.0.227",  'E');
    return 0;
}