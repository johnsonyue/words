import re

def new_form_rule(func, label):
	return {"func":func, "label":label}

class rule():
	def __init__(self):
		self.form_group_lt = {
			0:{"func":self._able, "label":"-able suffix"}
		}

	def _able(self,spelling):
		if re.findall("able$",spelling):
			return True
		return False
	
	def con_(self,spelling):
		if re.findall("^con",spelling):
			return True
		return False
