import sys

import lookup

def usage():
	print

def main(argv):
	if len(argv) < 2:
		usage()

	spelling = argv[1]
	lookup.lookup(spelling)

if __name__ == "__main__":
	main(sys.argv)
