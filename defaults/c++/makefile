CC = g++
CFLAGS = -c -Wall
INCLUDE = -Iinclude
LIBS =
OBJECTS = $(patsubst %,bin/%.o,$(NAMES))
NAMES = main

all: $(OBJECTS)
	$(CC) bin/*.o -o bin/test.exe $(INCLUDE) $(LIBS)
	@echo
	
bin/%.o: src/%.cpp
	$(CC) $< $(CFLAGS) -o $@ $(INCLUDE) $(LIBS)

clean:
	rm bin/*

new:
	mkdir bin

test: all
	bin/test.exe
