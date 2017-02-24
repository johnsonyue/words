import urllib2

import sources

#Data Structures.
def new_form(spelling, pronounce):
	return {"spelling":spelling, "pronounce":pronounce}

def new_word(spelling, pronounce, property, translation, examples):
	form = new_form(spelling, pronounce)
	return form, {"property":property, "translation":translation}

def new_form_rule(func, label):
	return {"func":func, "label":label, "forms":[]}

def new_word_rule(leader, label):
	return {"leader":leader, "label":label, "words":[]}

def new_sentence(sentence, label, ts, cnt):
	return {"sentence":sentence, "label":label, "ts":ts, "cnt":cnt}

form_group_lt = {}
word_group_lt = {}

#Knowledge Bank.
##nodes.
form_dict = {}
word_dict = {}
sentence_dict = {}
##links.
form_groups = {}
word_groups = {}

#Actions.
def lookup(spelling):
	words = query(spelling)
	if not words:
		print "Not a word"
		return

	interact(words)
	return words

def query(spelling):
	#todos: add more sources.
	base_url = sources.iciba_base_url
	parser = sources.iciba_parser()
	
	url = base_url + spelling
	request = urllib2.Request(url);
	request.add_header('User-agent','Mozilla/5.0');
	f = urllib2.urlopen(request);
	parser.feed(f.read())
	f.close()

	if parser.speak == "":
		return None

	words = []
	for k in range(1,len(parser.word.keys())+1):
		property = parser.word[str(k)][0]
		translation = {"ee":parser.word[str(k)][1], "ec":parser.word[str(k)][2]}
		examples = None
		if ( len(parser.word.keys()) > 3 ):
			examples = word[str(k)][3:]

		words.append( new_word(spelling,parser.speak,property,translation,examples) )

	return words

def match(words):
	#if word.cnt >= 1:
	#	inc_word(cnt+1,ts)
	#else:
	#	insert_word(word,relation)
	return ""

def relate(words):
	##todos: implement search functions.
	#fids=search_form(words)
	#wids=search_word(words)
	#sids=search_sentence(words)
	
	return ""
