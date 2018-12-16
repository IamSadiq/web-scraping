from bs4 import BeautifulSoup
import re

def readFile(pathToFile):
    file = open(pathToFile)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(readFile('my-pages/simple-page.html'), 'html.parser')

# print(soup.html.prettify())

# String parameter --- treats the string as a tag name & returns a list of of all the tags with the tag name present in the parse tree
print(soup.find_all('a'))
for tag in soup.find_all('a'):
    print(tag.name)

print('\n')
# regex parameter ---- passes the regex pattern to the find_all(regex) method and uses it to do its searching
regex = re.compile('^b') # match all tags that begins with 'b'
for tag in soup.find_all(regex):
    print(tag.name)

# print('\n')
# print(soup.find_all(re.compile('\w')))

print('\n')
# list parameter -- print all tag names present in the list argument
for tag in soup.find_all(['a','b', 'title', 'script']):
    print(tag.name)
    # print(tag.string)
    
print('\n')
# function parameter --- passes a function that it uses to perform some filtering
def has_class(tag):
    return tag.has_attr('class')

def has_id(tag):
    return tag.has_attr('id')

# print all tags with a 'class' attribute
for tag in soup.find_all(has_class):
    print(tag.name)

#print all tags with an 'id' attribute
for tag in soup.find_all(has_id):
    print(tag.name)