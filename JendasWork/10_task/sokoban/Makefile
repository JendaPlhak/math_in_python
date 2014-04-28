all: sokoban_dir solve gif clean

sokoban_dir:
	mkdir -p sokoban
	rm -f sokoban/*

solve:
	python sokoban_solver.py

gif:
	./create_gif.sh

clean:
	rm -Rf sokoban
