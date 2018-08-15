from bs4 import BeautifulSoup
import requests
from xlsxwriter import Workbook

# base_url = 'http://instagram.com'
base_url = 'http://eazetng.com'

workbook = Workbook('worksheets/instgram-images.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

worksheet.write('A0', "WEBSITE SUB-URLs", bold)
worksheet.write('F1', "IMAGE SOURCES", bold)


def get_hrefs(url):
    # make a get request and pull page content
    response = requests.get(url)
    
    # pulling the source code
    data = response.text

    # make soup
    soup = BeautifulSoup(data, 'html.parser')

    # Extracting all of the <a> tags into a List
    a_tags = soup.find_all('a')

    # save all <a> href's to a list
    all_href = [tag.get('href') for tag in a_tags if tag.get('href') is not None]
    return all_href

def get_img_srcs():
    srcList = []
    urls = get_hrefs(base_url)
    for url in urls:
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        img_tags = soup.find_all('img')
        
        for tag in img_tags:
            if tag.get('src') is not None:
                srcList.append(tag.get('src'))
        
    return srcList

# get all sites hyperlinks
siteHrefs = get_hrefs(base_url)
print('All site urls: ', len(siteHrefs))
print('\n',siteHrefs)

for row in range(len(siteHrefs)):
    worksheet.write(row+1,0,row)
    worksheet.write(row+1,1,siteHrefs[row])


# for row in range(len(bulkImages)):
#     worksheet.write(row+1,5,row)
#     worksheet.write(row+1,6,bulkImages[row])

# it's always a good practice to close the workbook
workbook.close()