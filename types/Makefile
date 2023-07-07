CC=gcc

all: gdbscript

import.h:
	touch $@

import.o: import.h
	$(CC) -g -fno-eliminate-unused-debug-types -x c -c -o $@ $<

gdbscript: import.o
	echo -n > $@
	echo 'add-symbol-file $<' >> $@

clean:
	rm *.o
