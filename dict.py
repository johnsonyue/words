import urllib2

import sources
import crud
import data_type

#Actions.
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

	form = data_type.new_form(spelling, parser.speak)
	
	words = []
	for k in range(1,len(parser.word.keys())+1):
		property = parser.word[str(k)][0]
		if ( len(parser.word[str(k)]) > 2 ):
			translation = {"ec":parser.word[str(k)][1], "ee":parser.word[str(k)][2]}
		else:
			translation = {"e*":parser.word[str(k)][1]}

		examples = None
		if ( len(parser.word[str(k)]) > 3 ):
			examples = parser.word[str(k)][3:]

		words.append( data_type.new_word(property,translation,examples) )

	return {"form":form, "words":words}

def match(crud, spelling):
	print "Matching "+spelling+" ... ",
	word = crud.retrieve(spelling)
	if not word:
		print "No Match"
		return False
	else:
		print "Match found"
		return True

def filter(rule, word):
	spelling = word["form"]["spelling"]
	print "Filtering "+spelling+" ... ",
	for k in rule.form_group_lt.keys():
		r = rule.form_group_lt[k]
		if r["func"](spelling):
			print "Filtered: " + r["label"]
			return k

	print "No match"
