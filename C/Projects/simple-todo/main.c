#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "todo.h"

int main()
{
    char tasks[MAX_TASKS][TASK_LEN];
    int count = 0;
    int choice, index;
    char input[TASK_LEN];

    load_tasks(tasks, &count, "tasks.txt");

    while (1) {
        printf("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Save and Exit\nChoice: ");
        scanf("%d", &choice);
        getchar(); // eat newlinei
        switch (choice) {
        case 1:
            print_tasks(tasks, count);
            break;
        case 2:
            printf("Enter Task: ");
            fgets(input, TASK_LEN, stdin);
            input[strcspn(input, "\n")] = 0; // removes newline
            add_task(tasks, &count, input);
            break;
        case 3:
            print_tasks(tasks, count);
            printf("Enter number of tasks to remove: ");
            scanf("%d", &index);
            getchar();
            remove_task(tasks, &count, index - 1);
            break;
        case 4:
            save_tasks(tasks, count, "tasks.txt");
            exit(0);
        default:
            printf("Please enter a valid option\n");
        }
    }
    return 0;
}
