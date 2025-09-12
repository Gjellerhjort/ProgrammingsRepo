#ifndef TODO_H
#define TODO_H

#define MAX_TASKS 100
#define TASK_LEN 128

void load_tasks(char tasks[][TASK_LEN], int *count, const char *filename);
void save_tasks(char tasks[][TASK_LEN], int count, const char *filename);
void add_task(char tasks[][TASK_LEN], int *count, const char *task);
void remove_task(char tasks[][TASK_LEN], int *count, int index);
void print_tasks(char tasks[][TASK_LEN], int count);

#endif
