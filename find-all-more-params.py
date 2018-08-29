from bs4 import BeautifulSoup
import re

def readFile(pathToFile):
    file = open(pathToFile)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(readFile('my-pages/simple-page.html'), 'lxml')

# STRING parameter --- expects a string attribute: soup.find_all(string='hey') OR a regex attribute: soup.find_all(re.compile('hey))
# and it returns a list of all the navigable strings containing the string or regex

# regex = re.compile('and')
regex = re.compile('siblings')
# regex = re.compile('Ricky')
# navStr = soup.find_all(string='Nicky')
navStr = soup.find_all(string=regex)
print(navStr)

# RECURSIVE parameter -- Boolean --- default is True and it permits deep descendants searching
# Seting recursive=False --- prevents descendants searching --- only permits direct children searching
print(soup.find_all('a', recursive=False)) #  returns empty list --- cos no direct child of soup is an 'a' tag
html = soup.html
print(html.find_all('head', recursive=False)) #  finds head as a direct child of html
print(html.find_all('title', recursive=False)) #  empty list --- as title is not a direct child of html
print(html.find_all('title', recursive=True)) #  finds title --- as the recursive param has being set to True as such descendants searching is enable
