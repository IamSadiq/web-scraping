from bs4 import BeautifulSoup as BS

def readFile(pathToFile):
    file = open(pathToFile)
    data = file.read()
    file.close()
    return data

soup = BS(readFile('my-pages/simple-page.html'), 'lxml')

# attrs filter --- accepts an attribute list and uses it to search the parse tree
attr = {'class':'links', 'id':'ricky'}
print(soup.find_all(attrs=attr))
print('\n\n')

attr = {'class':'paragraph hyperlinks'}
p_tags = soup.find_all('p', attrs=attr)
print(p_tags)

print(end='\n\n')
# limit filter ---- this accepts an integer and uses it to search the tree
a_tags = soup.find_all('a', limit=2)
print(a_tags)