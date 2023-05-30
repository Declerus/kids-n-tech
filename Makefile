Makefile

	install:
		# pip install -e .
		pip install pandas

	clean:
		rm -f */version.txt
		rm -f .coverage
		rm -f */.ipynb_checkpoints
		rm -Rf build
		rm -Rf */__pycache__
		rm -Rf */*.pyc

	all: install clean
