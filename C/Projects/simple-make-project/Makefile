# compiler to use
CC = gcc

# options for compiler
CFLAGS = -c -Wall

MYBINARY = program
OBJECTS = main.o insert_sort.o

#.PHONY: default
#default:
#	@cat helpfile

.PHONY: run
run:
	./$(MYBINARY)

all: prog

prog: $(OBJECTS)
	$(CC) $(OBJECTS) -o $(MYBINARY)

%.o: %.c
	$(CC) $(CFLAGS) $<

.PHONY: clean
clean:
	rm -fr *o

