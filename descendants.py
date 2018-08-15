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

# .contents -- returns a tag's direct children
children = [child for child in body.contents if child != '\n']
print('body.contents: ', len(children))
print(children)

print('\n\n')
# .descendants -- returns a tag's descendants, direct children's children. . .
descendants = [des for index,des in enumerate(body.descendants) if des != '\n']
print('body.descendants: ', len(descendants))
print(descendants)