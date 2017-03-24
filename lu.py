import sys

import lookup

def usage():
	print "python lu.py (query)"

def main(argv):
	if len(argv) < 1:
		usage()

	if len(argv) == 2:
		spelling = argv[1]
		lookup.lookup(spelling)
	elif len(argv) == 1:
		lookup.interact()

if __name__ == "__main__":
	main(sys.argv)
