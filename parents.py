from bs4 import BeautifulSoup

def readFile(theFile):
    file = open(theFile)
    data = file.read()
    file.close()
    return data

myFile = readFile('my-pages/simple-page.html')

soup = BeautifulSoup(myFile, 'lxml')
link = soup.a

# .parents -- returns a list (generator) of parents
for parent in link.parents:
    print(parent.name)
