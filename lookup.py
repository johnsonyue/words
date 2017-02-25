import dict
import crud
import rule

def lookup(spelling,kb_path):
	words = dict.query(spelling)
	if not words:
		print "Not a word"
		return

	interact(words,kb_path)
	return words

def usage():
	print "usage 1"

def usage2():
	print "usage 2"

def var_dump(var, prefix=''):
	if isinstance(var,type([])):
		for i in var:
			var_dump(i, prefix)
	elif isinstance(var,type({})):
		for k in var.keys():
			print prefix+k+':'
			var_dump(var[k], prefix+'    ')
	else:
		print prefix+str(var)
    
def list(word):
	var_dump(word["form"])
	var_dump(word["words"])

def interact(w,kb_path):
	crud_helper = crud.crud("/Users/john/python_workspace/words/kb")
	r = rule.rule()
	m = dict.match(crud_helper,w["form"]["spelling"])
	f = dict.filter(r,w)
	#list(w)

	is_edit = False
	while(True):
		print "> ",
		c = raw_input()
		
		if (c == "l"):
			list(w)
			continue

		if (is_edit):
			if (c == "q"):
				is_edit = False
			elif (c == "h"):
				usage2()
		else:
			if (c == "q"):
				break
			elif (c == "h"):
				usage()
			elif (c == "e"):
				is_edit = True
			elif (c == "c"):
				crud_helper.create(w)
			elif (c == "x"):
				crud_helper.export("/Users/john/python_workspace/words/kb")

	return ""
