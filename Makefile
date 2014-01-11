all:
	mkdir -p build
	./make.py

clean:
	rm -rfv build/ *.pyc
