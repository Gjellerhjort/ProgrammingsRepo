#include "todo.h"
#include <stdio.h>
#include <string.h>

void load_tasks(char tasks[][TASK_LEN], int *count, const char *filename)
{
    FILE *file = fopen(filename, "r");
    *count = 0;
    if(!file) return;
    while (fgets(tasks[*count], TASK_LEN, file) && *count < MAX_TASKS) {
        tasks[*count][strcspn(tasks[*count], "\n")] = 0;
        (*count)++;   
    }
    fclose(file);
}

void save_tasks(char tasks[][TASK_LEN], int count, const char *filename)
{
    FILE *file = fopen(filename, "w");
    if (!file) {
        printf("Could not open file for writing\n");
        return;
    }
    for (int i = 0; i < count; i++) {
        fprintf(file, "%s\n", tasks[i]);
    }
    fclose(file);
}

void add_task(char tasks[][TASK_LEN], int *count, const char *task)
{
    if (*count < MAX_TASKS) {
        strncpy(tasks[*count], task, TASK_LEN -1);
        tasks[*count][TASK_LEN - 1] = '\0';
        (*count)++;
    }
}

void remove_task(char tasks[][TASK_LEN], int *count, int index) 
{
    if (index < 0 || index >= *count) return;
    for (int i = 0; i < *count - 1; i++) {
        strncpy(tasks[i], tasks[i+1], TASK_LEN);
    }
    (*count)--;
}

void print_tasks(char tasks[][TASK_LEN], int count)
{
    printf("Todo list:\n");
    for (int i = 0; i < count; i++) {
        printf("%d. %s\n", i+1, tasks[i]);
    }
}


