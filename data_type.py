#Data Structures.
def new_form(spelling, pronounce):
	return {"spelling":spelling, "pronounce":pronounce}

def new_word(property, translation, examples):
	return {"property":property, "translation":translation, "examples":examples}

def new_word_rule(leader, label):
	return {"leader":leader, "label":label}

def new_sentence(sentence, label, ts, cnt):
	return {"sentence":sentence, "label":label}
