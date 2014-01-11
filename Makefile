all:
	mkdir -p build
	./src/make.py

clean:
	rm -rfv build/ ./src/*.pyc
