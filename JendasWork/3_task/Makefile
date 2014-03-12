PCC   = cython
GCC   = clang
FLAGS = -shared -fPIC -fno-strict-aliasing -fwrapv -O3 -Wall -Wextra -L. -I/usr/include/python2.7

PYXS = $(wildcard *.pyx)
OBJS = $(PYXS:.pyx=.so)

TMP = temp_file.code

all: $(OBJS)

%.so: %.pyx Makefile
	$(PCC) -o $(TMP) $<
	$(GCC) -x c $(FLAGS) -o $@ $(TMP)
	rm -f $(TMP)
	strip $@

clean:
	rm -f *.so $(TMP)
	rm -f *.pyc

.PHONY: all clean
