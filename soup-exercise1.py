from bs4 import BeautifulSoup
import requests

url = 'http://localhost/breakoutmuzic/'

# Getting the webpage, creating a response object
response = requests.get(url)

# status code
print('status code: ', response.status_code)

# response headers
headers = response.headers

for key, value in headers.items():
    print(key, '   ', value)

# Extracting the source code of the webpage
data = response.text

# Passing the sorce code to BeautifulSoup to create an object of it
soup = BeautifulSoup(data, 'html.parser')

# Extracting all of the <a> tags into a List
tags = soup.find_all('a')

# length of list
print('total <a> tags: ', len(tags))

# Extracting urls from the attribute href in the <a> tags
for tag in tags:
    print(tag.get('href'))
