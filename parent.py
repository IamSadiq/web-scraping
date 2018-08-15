'''
.parent --- returns the direct parent (Goes Up the parse tree) of a tag and it's content(children & descendants)
.name --- returns the name (string) of a tag (withouth its content)
bs4 is the parent of every tag in a parse tree and it has no parent
'''
from bs4 import BeautifulSoup

def readFile(theFile):
    file = open(theFile)
    data = file.read()
    file.close()
    return data

myFile = readFile('my-pages/simple-page.html')

soup = BeautifulSoup(myFile, 'lxml')
# print(soup.contents)
p = soup.p
# print(p)

# .parent --- returns the parent of a tag
# print p tag's direct parent (body) and its content
# print(p.parent)

# .name -- returns the parent tag's name
# print(p.parent.name)

html = soup.html
print(type(html.parent))