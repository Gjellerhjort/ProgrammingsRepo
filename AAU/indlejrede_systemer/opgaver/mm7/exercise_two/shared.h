#ifndef SHARED_H
#define SHARED_H

#define SHARED_MEM_NAME "/myName"

struct shared_memory {
    char buf[256];
    int buffer_length;
};

#endif

