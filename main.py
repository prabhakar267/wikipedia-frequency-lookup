# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-04-18 03:00:45
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-04-20 11:47:34

from bs4 import BeautifulSoup
import requests
import re
import operator
import json
from tabulate import tabulate


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



wikipedia_api_link = "https://en.wikipedia.org/w/api.php?format=json&action=query&list=search&srsearch="
wikipedia_link = "https://en.wikipedia.org/wiki/"

string_query = raw_input("aloo")

url = wikipedia_api_link + string_query
response = requests.get(url)

data = json.loads(response.content)
wikipedia_page_tag = data['query']['search'][0]['title']

url = wikipedia_link + wikipedia_page_tag
page_word_list = getWordList(url)
page_word_count = createFrquencyTable(page_word_list)

sorted_word_frequency_list = sorted(page_word_count.items(), key=operator.itemgetter(1), reverse=True)
if len(sorted_word_frequency_list) > 10:
	sorted_word_frequency_list = sorted_word_frequency_list[:10]

print_headers = ['Word', 'Frequency']

print tabulate(sorted_word_frequency_list, headers=print_headers, tablefmt='orgtbl')
