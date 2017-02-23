//Data Structures.
def new_form(spelling, pronounce):
	return {"spelling":spelling, "pronounce":pronounce}

def new_word(spelling, pronounce, property, tranlation):
	form = new_form(spelling, pronounce)
	return {"form":form, "property":property, "translation":translation, "ts":ts, "cnt":cnt}

def new_form_rule(func, label):
	return {"func":func, "label":label, "forms":[]}

def new_word_rule(leader, label, ts, cnt):
	return {"leader":leader, "label":label, "words":[]}

def new_sentence(sentence, label, ts, cnt):
	return {"sentence":sentence, "label":label, "ts":ts, "cnt":cnt}

form_group_lt = {}
word_group_lt = {}

//Knowledge Bank.
////nodes.
form_dict = {}
word_dict = {}
sentence_dict = {}
////links.
form_groups = {}
word_groups = {}

//Actions.
def lookup(spelling):
	print ("Looking up " + spelling)
	//todos: find source, parse source to word
	print ("Done.")
	return word

def relate(word):
	//todos: implement search functions.
	fids=search_form(word)
	wids=search_word(word)
	sids=search_sentence(word)
	
	return {}

def add_word(spelling):
	word = lookup(spelling)
	if not word:
		//todos: implement not_word()
		not_word()
	else:
		//todos: implemets crud.
		if word.cnt >= 1:
			inc_word(cnt+1,ts)
		else:
			relation = relate(word)
			insert_word(word,relation)
