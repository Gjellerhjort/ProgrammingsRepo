#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>

#include "shared.h"

int main(void) {
    int fd;
    struct shared_memory *shared;

    fd = shm_open(SHARED_MEM_NAME, O_RDWR, 0666);
    if (fd == -1) {
        perror("shm_open failed - server must be running first");
        exit(1);
    }

    shared = mmap(NULL, sizeof(struct shared_memory), 
                  PROT_READ | PROT_WRITE,  MAP_SHARED, fd, 0);
    if (shared == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(1);
    }

    printf("Client ready. Type messages (type 'stop' to quit)\n\n");

    char local_buf[256];

    while (1) {
        printf("please type a message: >>");
        fflush(stdout);

        if (fgets(local_buf, sizeof(local_buf), stdin) == NULL) {
            break;
        }
        // remove trailing newline
        local_buf[strcspn(local_buf, "\n")] = '\0';
        // check for stop command
       // message preparation
        strncpy(shared->buf, local_buf, sizeof(shared->buf) - 1);
        shared->buf[sizeof(shared->buf) - 1] = '\0';
        shared->buffer_length = strlen(shared->buf) + 1;

        printf("Sent: %s\n", local_buf);

        if (strcmp(local_buf, "stop") == 0) {
            printf("Client shutting down...\n");
            break;
        }
 
    }

    munmap(shared, sizeof(struct shared_memory));
    close(fd);

    printf("Client terminated.\n");
    return 0;
}
