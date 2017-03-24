import dict
import crud
import rule

def lookup(spelling):
	words = dict.query(spelling)
	if not words:
		print "Not a word"
		return

	interact(words)
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
	print "meanings:"
	for i in range(len(word["words"])):
		print "  "+str(i)+":"
		var_dump(word["words"][i], prefix="    ")

def interact(w=None):
	if w:
		crud_helper = crud.crud("/Users/john/python_workspace/words/kb")
		r = rule.rule()
		m = dict.match(crud_helper,w["form"]["spelling"])
		f = dict.filter(r,w)
		list(w)
	else:
		crud_helper = crud.crud("/Users/john/python_workspace/words/kb")

	is_edit = False
	is_review = False
	while(True):
		if (not w):
			is_edit = False
			is_review = True
		if (is_edit):
			print "#edit> ",
		elif(is_review):
			print "#review> ",
		else:
			print "#query> ",
			
		c = raw_input()

		if (is_edit):
			if (c == "q"):
				is_edit = False
			elif (c == "h"):
				usage2()
		elif (is_review):
			if (c == "q"):
				if (not w):
					break
				is_review = False
			if (c == "l"):
				crud_helper.list()
		else:
			if (c == "q"):
				break
			elif (c == "h"):
				usage()
			elif (c == "l"):
				list(w)
			elif (c == "a"):
				crud_helper.create(w)
				crud_helper.export("/Users/john/python_workspace/words/kb")
				break
			elif (c == "e"):
				is_edit = True
			elif (c == "r"):
				is_review = True
			elif (c == "c"):
				crud_helper.create(w)
			elif (c == "x"):
				crud_helper.export("/Users/john/python_workspace/words/kb")

	return ""
