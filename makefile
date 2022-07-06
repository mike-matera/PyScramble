
OUTPUTDIR ?= $(realpath .)

all: pydist 

pydist: $(OUTPUTDIR)
	python3 ./setup.py sdist -d $(OUTPUTDIR)/dist > /dev/null

clean:
	-rm -rf ./dist PyScramble.egg-info

.PHONY: all pydist clean
