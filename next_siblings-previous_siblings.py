from bs4 import BeautifulSoup

def readFile(theFile):
    file = open(theFile)
    data = file.read()
    file.close()
    return data

myFile = readFile('my-pages/simple-page.html')

soup = BeautifulSoup(myFile, 'lxml')
body = soup.body

p = body.p

# .next_siblings -- returns a generator / list of all the next siblings forward of the current tag
for sibling in p.next_siblings:
    if sibling.name is not None:
        print(sibling.name)

print('\n')

# .previous_siblings -- returns a generator / list of all the previous siblings backwards of the current tag
for sibling in p.previous_siblings:
    if sibling.name is not None:
        print(sibling.name)