# -*- coding: utf-8 -*-
import HTMLParser
import re

iciba_base_url = "http://www.iciba.com/"

class iciba_parser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		
		self.is_collins = False
		self.is_class = False
		self.nest_cnt = 0
		self.speak = ""
		self.number = ""
		self.word = {}

	def handle_starttag(self, tag, attrs):
		if (tag == "div" and self.get_attr_value("class",attrs) == "info-article"):
			self.is_class = True
		elif (tag == "div" and self.is_class):
			self.nest_cnt += 1
		
	def handle_endtag(self, tag):
		if (tag == "div" and self.nest_cnt):
			self.nest_cnt -= 1
		elif (tag == "div" and self.is_class):
			self.is_class = False
		
		if (self.is_collins and not self.is_class):
			self.is_collins = False

	def get_attr_value(self, target, attrs):
		for e in attrs:
			key = e[0]
			value = e[1]
			if (key == target):
				return value
		return ""

	def handle_data(self, data):
		if (data.replace('\n','').replace('\t','').replace(' ','').replace('\n\r','') == ""):
			return

		if (re.findall("^美.*]$", data) or re.findall(".*]$", data)): 
			self.speak = data

		if ( self.is_collins and re.findall("^[0-9]", data) ):
			self.number = data
			self.word[self.number] = []
		elif ( self.is_collins ):
			self.word[self.number].append(data)

		if (self.is_class and re.findall("柯林斯", data)):
			self.is_collins = True
