
CC = gcc
CFLAGS = -c -Wall
OBJECTS = main.o todo.o
TARGET = todo

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -rf $(TARGET) *.o
