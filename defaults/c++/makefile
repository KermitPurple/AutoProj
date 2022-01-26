# Last updated 2022-01-25 by Shane McDonough
CC=clang#c compiler
EXTENSION=.c#c extension
TARGET=bin/test#the output file
DBG_TARGET=$(TARGET).debug
FLAGS=-Wall -Iinclude#flags to be passed to compiler
DBG_FLAGS=-g#flags for debugging
ifeq ("$(wildcard src/*$(EXTENSION))", "")#if there are no c files
	CC=clang++#c++ compiler
	EXTENSION=.cpp#c++ extension
	FLAGS+=-std=c++20#c++ flags
endif
INCLUDES=$(wildcard include/*)# get all include files
OBJECTS=$(patsubst src/%$(EXTENSION),bin/%.o,$(wildcard src/*$(EXTENSION)))# in bin/%.o format, all of the objects to be compiled
DBG_OBJECTS=$(patsubst %,%.debug,$(OBJECTS))

all: $(OBJECTS)# compile everything
	$(CC) bin/*.o $(FLAGS) -o $(TARGET)
	
bin/%.o: src/%$(EXTENSION) $(INCLUDES) bin# create object file for %
	$(CC) $< $(FLAGS) $(DBG_FLAGS) -c -o $@

clean:# remove contents of bin
	rm -rf bin

bin:# create folder bin
	mkdir bin

test: all# compile everything then run executible
	$(TARGET)

debug: $(DBG_TARGET)# run make with debug flags and call lldb
	lldb $(DBG_TARGET)

$(DBG_TARGET): $(DBG_OBJECTS) $(INCLUDES)# create debug executable
	$(CC) bin/*.o.debug $(FLAGS) $(DBG_FLAGS) -o $@

bin/%.o.debug: src/%$(EXTENSION) $(INCLUDES) bin# create debug object file for %
	$(CC) $< $(FLAGS) $(DBG_FLAGS) -c -o $@

.PHONY: all clean test debug
