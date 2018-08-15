from bs4 import BeautifulSoup

def readFile(theFile):
    file = open(theFile)
    data = file.read()
    file.close()
    return data

myFile = readFile('my-pages/simple-page.html')

soup = BeautifulSoup(myFile, 'lxml')
body = soup.body

# .previous_sibling --- moves sideways to the previous sibling (backwards) of the current tag in a parse tree
# again bcos of the newline (/n) character we have to call it twice
print(body.previous_sibling.previous_sibling)