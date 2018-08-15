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
title = soup.title

# print tag's navigable string
print(title.string)

# Replacing a tag's Navigable Strings -- using replace_with(string_to_replace_with)
title.string.replace_with('Web Scraping Tutorial')
print(title.string)