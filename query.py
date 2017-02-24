import sys
import urllib2

import dict_utils
import sources

def main(argv):
	spelling = argv[1]

	#todos: add more sources.
	base_url = sources.iciba_base_url
	parser = sources.iciba_parser()
	
	url = base_url + spelling
	request = urllib2.Request(url);
	request.add_header('User-agent','Mozilla/5.0');
	f = urllib2.urlopen(request);
	parser.feed(f.read())
	f.close()

	print parser.speak
	#print parser.word
	for k in range(1,len(parser.word.keys())+1):
		for i in range(len(parser.word[str(k)])):
			print parser.word[str(k)][i]
		print

if __name__ == "__main__":
	main(sys.argv)
