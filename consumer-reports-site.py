from bs4 import BeautifulSoup

def read_file():
    file = open('txt/consumer-reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'html.parser')
# print(soup.text)

# product_names = [div.div.a.span.string for div in soup.find_all('div', class_='entry-letter')]
# product_links = [div.div.a['href'] for div in soup.find_all('div', class_='entry-letter')]

products = [{div.div.a.span.string:div.div.a['href']} for div in soup.find_all('div', class_='entry-letter')]
# print(products)

file = open('./txt/products.json', 'w')
file.write(str(products))
file.close()


# for key, value in products.items():
#     print(key, ':   ', value)

