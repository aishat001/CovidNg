#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


#r = learrequests.get('https://covid19.ncdc.gov.ng/').text

# if r.status_code == 200:
# 	soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")

# 	for item in soup.find_all("table", {"custom1": "tr"}):
# 		print(item.text)
tab = []
url = 'covid2.html'
#url = requests.get('https://covid19.ncdc.gov.ng/')
#soup = BeautifulSoup(url.content, 'html.parser')
soup = BeautifulSoup(open(url), 'html.parser')
custom1 = soup.find(class_ = 'text-right text-white')
# tr = custom1.find_all('tr')
# print(tr.text)

confirmed_cases = custom1.text
active_cases = soup.find_all('h2')


tab.append({
	'Samples Tested': active_cases[0].text[2:],
	'confirmed_cases': active_cases[1].text,
	'Active Cases': active_cases[2].text,
	'Discharged Cases': active_cases[3].text,
	'Death': active_cases[4].text})

for item in tab:
	for k, v in item.items():
		print(k, ': ', v)