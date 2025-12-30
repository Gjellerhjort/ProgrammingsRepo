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

    fd = shm_open(SHARED_MEM_NAME, O_CREAT | O_RDWR, 0666);
    if (fd == -1) {
        perror("shm_open failed");
        exit(1);
    }

    if (ftruncate(fd, sizeof(struct shared_memory)) == -1) {
        perror("ftruncate failed");
        close(fd);
        exit(1);
    } 

    shared = mmap(NULL, sizeof(struct shared_memory), 
                  PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (shared == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        exit(1);
    }

    shared->buffer_length = 0;
    shared->buf[0] = '\0';

    printf("Server stated. Waiting for messages...\n"
           "Will exit when clients sends stop\n"
           );
    while (1) {
        if (shared->buffer_length > 0) {
            char local_buf[256];
            strncpy(local_buf, shared->buf, sizeof(local_buf) -1);
            local_buf[sizeof(local_buf) - 1] = '\0';
            
            printf("Received: %s\n", local_buf);

            if (strcmp(local_buf, "stop") == 0) {
                printf("Received 'stop' command from client\n");
                shared->buffer_length = 0;
                break;
            }

            shared->buffer_length = 0;
        }

        sleep(1);
    }

    // Cleanup
    close(fd);
    shm_unlink(SHARED_MEM_NAME);

    printf("Server terminated.\n");
    return 0;
}
