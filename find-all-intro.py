from bs4 import BeautifulSoup as BS

def readFile(pathToFile):
    file = open(pathToFile)
    data = file.read()
    file.close()
    return data

soup = BS(readFile('my-pages/simple-page.html'), 'lxml')

# find_all function parameters -> Signature: find_all(name, attrs, limit, recursive, string, **kwargs)
# name parameter --- string parameter
print(soup.find_all('a'))
print('\n\n')

# attrs parameter --- filter --- accepts an attribute dictionary and uses it to search the parse tree
attr = {'class':'links', 'id':'ricky'}
print(soup.find_all(attrs=attr))
print('\n\n')

attr = {'class':'paragraph hyperlinks'}
p_tags = soup.find_all('p', attrs=attr)
print(p_tags)

print(end='\n\n')
# limit parameter --- filter ---- this accepts an integer and uses it to search the tree
a_tags = soup.find_all('a', limit=2)
print(a_tags)