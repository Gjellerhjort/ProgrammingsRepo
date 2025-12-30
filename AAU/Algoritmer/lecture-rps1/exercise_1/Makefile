CC = gcc
CFLAGS = -Wall -Wextra -Wpedantic -Werror -std=c17
SRC = main.c
OUT = main

.PHONY: all clean

all: $(OUT)

$(OUT): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(OUT)

clean:
	rm -f $(OUT)
