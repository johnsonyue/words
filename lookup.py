import dict_utils

def usage():
	print "usage 1"

def usage2():
	print "usage 2"

def list(word, match, relation):
	print word
	print "list"

def create(word):
	return ""

def update(word):
	return ""

def delete(word):
	return ""

def interact(words):
	w = words
	m = match(w)
	r = relate(w)
	list(w,m,r)

	is_edit = False
	while(True):
		print "> ",
		c = raw_input()
		
		if (c == "l"):
			list(w,m,r)
			continue

		if (is_edit):
			if (c == "q"):
				is_edit = False
			elif (c == "h"):
				usage2()
			elif (c == "c"):
				w = create(w)
			elif (c == "u"):
				w = update(w)
			elif (c == "d"):
				w = delete(w)
		else:
			if (c == "q"):
				add()
				break
			elif (c == "h"):
				usage()
			elif (c == "e"):
				is_edit = True
			elif (c == "a"):
				add()
		
	return ""
