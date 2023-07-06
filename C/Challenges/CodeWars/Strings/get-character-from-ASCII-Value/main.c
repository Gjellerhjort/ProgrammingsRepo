#include <stdio.h>

char char_of_code (unsigned charcode)
{
  return  (char)charcode;
}

void do_test(int charcode, char expected)
{
    char actual = char_of_code(charcode);
    printf("Charcode: %d Got: %c Expected: %c \n",charcode,actual,expected);
}

int main()
{
  do_test(55, '7');
  do_test(56, '8');
  do_test(57, '9');
  do_test(58, ':');
  do_test(59, ';');
  do_test(60, '<');
  do_test(61, '=');
  do_test(62, '>');
  do_test(63, '?');
  do_test(64, '@');
  do_test(65, 'A');
  do_test(0, '\0');
  do_test(127, '\x7f');
}