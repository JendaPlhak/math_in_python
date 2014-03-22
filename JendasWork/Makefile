DIRS = 3_task 4_task

all: subdirs

subdirs:
	-for d in $(DIRS); do ($(MAKE) -C $$d all); done    
clean:
	-for d in $(DIRS); do ($(MAKE) -C $$d clean); done  

.PHONY: all clean