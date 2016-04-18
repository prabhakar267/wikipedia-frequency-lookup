# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-04-18 03:00:45
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-04-18 23:14:51

from bs4 import BeautifulSoup
import requests
import re
import operator


def getWordList(url):
	word_list = []
	
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,'lxml')
	
	for text in soup.findAll('p'):
		if text.text is None:
			continue

		content = text.text
		words = content.lower().split()

		for word in words:
			cleaned_word = clean_word(word)

			if len(cleaned_word) > 0:
				word_list.append(cleaned_word)

	return word_list



def clean_word(word):
	cleaned_word = re.sub('[^A-Za-z]+', '', word)
	return cleaned_word



def createFrquencyTable(word_list):
	word_count = {}

	for word in word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

	return word_count



wikipedia_link = "https://en.wikipedia.org/wiki/Martin_Luther_King,_Jr."
page_word_list = getWordList(wikipedia_link)
page_word_count = createFrquencyTable(page_word_list)

sorted_word_frequency_list = sorted(page_word_count.items(), key=operator.itemgetter(1), reverse=True)
if len(sorted_word_frequency_list) > 10:
	sorted_word_frequency_list = sorted_word_frequency_list[:10]

for key, value in sorted_word_frequency_list:
	print('"' + str(key) + '" \t- ' + str(value) + " times")
