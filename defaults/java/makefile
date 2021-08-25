MAIN=Main
SRCS=$(wildcard *.java)
CLSS=$(patsubst %.java,%.class, $(SRCS))
JCARGS=

all: $(CLSS)
	@echo [[Compiled]]

%.class: %.java
	javac $(JCARGS) $<

test: all
	java $(MAIN)

clean:
	rm -rf *.class
