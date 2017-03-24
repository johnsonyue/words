import pickle

import data_type

class crud():
	def __init__(self,kb_file=""):
		##nodes.
		self.form_dict = {}
		self.word_dict = {}
		self.sentence_dict = {}
		##links.
		self.form_groups = {}
		self.word_groups = {}
		
		print "Loading KB ...",
		if kb_file != "":
			self.load_kb(kb_file)
		print " Done"
	
	def load_kb(self,kb_file):
		f=open(kb_file, 'rb')
		#kb = json.loads(f.read())
		kb = pickle.load(f)
		self.form_dict = kb["form_dict"]
		self.word_dict = kb["word_dict"]
		self.sentence_dict = kb["sentence_dict"]
		self.form_groups = kb["form_groups"]
		self.word_groups = kb["word_groups"]
	
	def create(self,word):
		form = word["form"]
		words = word["words"]
		
		form_key = 0 if not self.form_dict else max(self.form_dict.keys())+1
		self.form_dict[form_key] = form
		self.form_dict[form_key]["word_key_list"] = []

		max_words = 0 if not self.word_dict else max(self.word_dict.keys())+1
		for i in range(len(words)):
			word_key = max_words + i
			words[i]["form_key"] = form_key
			self.word_dict[word_key] = words[i]
			
			self.form_dict[form_key]["word_key_list"].append(word_key)
	
	def retrieve(self,spelling):
		word_key_list = None
		form_key = None

		for k in self.form_dict.keys():
			form = self.form_dict[k]
			if form["spelling"] == spelling:
				word_key_list = self.form_dict[k]["word_key_list"]
				form_key = k
				break

		if form_key == None:
			return None

		words = []
		for i in range(len(word_key_list)):
			k = word_key_list[i]
			words.append(self.word_dict[k])

		word = {"words":words, "form":self.form_dict[form_key]}
		
		return word
	
	def update(self):
		return ""
		
	def delete(self,spelling):
		word_key_list = None
		form_key = None
		for k in self.form_dict.keys():
			form = self.form_dict[k]
			if form.spelling == spelling:
				word_key_list = self.form_dict[k]["word_key_list"]
				form_key = k
				break

		if not word_key_list:
			return False

		for i in range(len(word_key_list)):
			k = word_key_list[i]
			self.word_dict.pop(k)

		self.form_dict.pop(form_key)
		
		return True
	
	def export(self,dst_path):
		kb={"form_dict":self.form_dict, "word_dict":self.word_dict, "sentence_dict":self.sentence_dict, "form_groups":self.form_groups, "word_groups":self.word_groups}
		f=open(dst_path,'wb')
		#f.write(json.dumps(kb, dst_path))
		pickle.dump(kb,f)
		return ""
		
	def sync(self):
		return ""

	
	def list(self):
		print "Total: "+str(len(self.form_dict.keys()))+" words"
		for k in sorted(self.form_dict.keys()):
			spelling = self.form_dict[k]["spelling"]
			pronounce = self.form_dict[k]["pronounce"]
			print "    "+spelling+'\t'+pronounce
			word_key_list = self.form_dict[k]["word_key_list"]
			for w in word_key_list:
				property = self.word_dict[w]["property"]
				translation = self.word_dict[w]["translation"]
				t = ""
				if translation.has_key("ec"):
					t = translation["ec"]
				elif translation.has_key("e*"):
					t = translation["e*"]
				
				print "      "+property+'\t'+t
