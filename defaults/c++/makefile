# Last updated 2021-9-3 by Shane McDonough
CC=clang++#compiler
EXTENSION=.cpp#c++ extension
FLAGS=-Wall -Iinclude#flags to be passed to compiler
OBJECTS=$(patsubst src/%$(EXTENSION),bin/%.o,$(wildcard src/*$(EXTENSION)))# in bin/%.o format, all of the objects to be compiled
# previous line explained:
# patsubst replaces the first arg template with the second arg template on the variable in the third arg
# wildcard gets all the files that comply with its arg
# in this case wildcard returns every file with the main extension in the src directory
# e.g. src/main.cpp src/File1.cpp
# patsub replaces the src and the extension
# e.g. bin/main.o bin/File1/.o

all: bin $(OBJECTS)# compile everything
	$(CC) bin/*.o $(FLAGS) -o bin/test
	
bin/%.o: src/%$(EXTENSION)# create object file for %
	$(CC) $< $(FLAGS) -c -o $@

clean:# remove contents of bin
	rm -rf bin

bin:# create folder bin
	mkdir bin

test: all# compile everything then run executible
	bin/test
