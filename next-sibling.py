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

print(p)
# .next_sibling -- moves sideways to the next sibling (forward) of the current tag in a parse tree
# however bcos of the newline (\n) character we might have to call it twice
print(p.next_sibling.next_sibling)