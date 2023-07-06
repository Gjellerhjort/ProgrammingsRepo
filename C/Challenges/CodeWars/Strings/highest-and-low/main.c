#include <stdio.h>
#include <string.h>

#define MAX_ELEMENTS 10

void high_and_low (const char *strnum, char *result)
{
// print your answer to result
    int array[MAX_ELEMENTS];
    int num_elements = 0;
    
    char buffer[strlen(strnum) + 1];
    strcpy(buffer, strnum);
    // Parse the string and store the integers in the array
    int num;
    char* token = strtok(buffer, " ");
    while (token != NULL && num_elements < MAX_ELEMENTS) {
        sscanf(token, "%d", &num);
        array[num_elements] = num;
        num_elements++;
        token = strtok(NULL, " ");
    }
    
    int max = -2147483647;
    int min = 2147483647;
    for (int i = 0; i < num_elements; i++) {
        if(max < array[i])
        {
            max = array[i];
        }
        if(min > array[i])
        {
            min = array[i];
        }
    }
	sprintf(result, "%d %d", max,min);
}

void do_test(const char *strnum, const char *expected)
{
    char result[20];
    high_and_low(strnum, result);
    printf("Got %s expected %s \n", result,expected);
}

int main() 
{
    do_test("8 3 -5 42 -1 0 0 -9 4 7 4 -4", "42 -9");
	do_test("1 2 3", "3 1");
}
