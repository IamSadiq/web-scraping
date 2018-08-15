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
meta = soup.meta
title = soup.title
body = soup.body

# print(meta)
# print(title)
# print(body)

# tag methods -- use get() ie tag.get('attribute) -- OR -- treat tag as a dictionary ie tag['attribute]
print(meta.get('charset'))

# Modify tag attributes
body['style'] = 'somebody'
print(body.get('style'))

# Accessing Multi-valued attributes -- Multi valued tags return a list of the attributes
print(body['class'])

# soup prettify
# print(soup.prettify())