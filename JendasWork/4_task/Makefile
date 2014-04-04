OBJS = skryvacka1.png skryvacka2.png skryvacka3.png

all: $(OBJS)

%.png:
	wget -O "img/$@" http://www.fi.muni.cz/~xpelanek/IV122/zadani/$@
	touch img/$@

clean:
	rm -f img/skryvacka*

cleanImg:
	rm -R img

.PHONY: all clean cleanImg