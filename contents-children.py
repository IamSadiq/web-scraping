from bs4 import BeautifulSoup

def readFile(input_file):
    file = open(input_file)
    data = file.read()
    file.close()
    return data

html_file = readFile('./my-pages/simple-page.html')

# Make a soup out of the html file
soup = BeautifulSoup(html_file, 'html.parser')

# Accessing tags
body = soup.body

print('\n-------------- tag.contents ---------------------')
# tag.contents -- returns a list of all tag children
for child in body.contents:
    print(child if child is not None else '', end='\n')

print('\n-------------- tag.children ---------------------')
# tag.children -- returns an iterator -- in scenario where the tree is very deep
for child in body.children:
    print(child if child is not None else '', end='\n')