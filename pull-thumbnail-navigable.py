from bs4 import BeautifulSoup
import re

def readFile(pathToFile):
    file = open(pathToFile)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(readFile('my-pages/js-page.html'), 'lxml')
body = soup.body
regex = re.compile('thumbnail_src')

for item in soup.find_all(string=regex):
    print(item, end='\n')