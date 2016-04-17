# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-04-18 03:00:45
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-04-18 03:12:49

from bs4 import BeautifulSoup
import requests
import re


def clean_word(word):
	cleaned_word = re.sub('[^A-Za-z]+', '', word)
	return cleaned_word


wikipedia_link = "https://en.wikipedia.org/wiki/Martin_Luther_King,_Jr."
word_list = []


source_code = requests.get(wikipedia_link)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')


count = 1
for text in soup.findAll('p'):
	if text.text is None:
		continue

	content = text.text
	words = content.lower().split()

	for word in words:
		cleaned_word = clean_word(word)

		if len(cleaned_word) > 0:
			word_list.append(cleaned_word)
			print(cleaned_word)

			count += 1


print(count)
