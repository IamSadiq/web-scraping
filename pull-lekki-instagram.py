from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
from xlsxwriter import Workbook
import re


ua = UserAgent()
base_url = 'https://www.instagram.com/lekki.ng/'
header = {'user-agent': ua.chrome}

# workbook = Workbook('worksheets/instagram-images.xlsx')
# worksheet = workbook.add_worksheet()
# bold = workbook.add_format({'bold': True})

response = requests.get(base_url, headers=header)

# pulling the source code
# data = response.text

# make soup
soup = BeautifulSoup(response.content, 'lxml')
# script = soup.find('script')
script = soup.body.script


window = {'_sharedData': "Hello"}

print(window['_sharedData'])

window['_sharedData'] = script.text

print(window['_sharedData'])

# soup prettify
# print(script.prettify())
# pattern = re.compile("(\w+): '(.*?)'")
# fields = dict(re.findall(pattern, script.text))
# print(fields)

# it's always a good practice to close the workbook
# workbook.close()