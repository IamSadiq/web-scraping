from bs4 import BeautifulSoup
import requests
import sys

res = requests.get('https://codingbat.com/prob/p181646')
page = res.text

soup = BeautifulSoup(page, 'html.parser')

div = soup.find('div', class_='minh')
print(div.string)

print(div.next_sibling.next_sibling.encode("utf-8"))
print(div.next_sibling.next_sibling.next_sibling.next_sibling.encode("utf-8"))
print(div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.encode("utf-8"))

# print(div.parent.encode("utf-8"))