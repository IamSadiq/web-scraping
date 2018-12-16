import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
header = {'user-agent': ua.chrome}
# print(ua.chrome)

page = requests.get('https://www.fxstreet.com/economic-calendar', headers=header)
print(page.content)
soup = BeautifulSoup(page.content, 'lxml')
# print(soup.encode('utf-8'))

fxst_general_div = soup.find('div', _class="sf_colsIn")
# print(fxst_general_div.encode('utf-8'));
# print(fxst_general_div)