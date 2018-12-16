from bs4 import BeautifulSoup
import requests
import re
import csv
from xlsxwriter import Workbook

workbook = Workbook('./worksheets/cb.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

regex = re.compile('/prob/p')
attr = {'href':regex}

base_url = 'https://codingbat.com'

def makeHttpRequest(url):
    response = requests.get(url)
    page = response.content
    return BeautifulSoup(page, 'lxml')

def doStage2(myList):
    newList = []
    for item in myList:
        # print(base_url + item)
        soup = makeHttpRequest(base_url + item)

        for tag in soup.find_all('a', attrs=attr):
            newList.append(tag['href'])

    return newList

def doStage3(myList):
    questions = []
    examples = []

    for item in myList:
        print(base_url + item)
        soup = makeHttpRequest(base_url + item)
        
        div = soup.find('div', class_='minh')
        questions.append(div.string)
        
        siblings = div.next_siblings
        examples = [sibling.encode('utf-8') for sibling in siblings if sibling.string is not None]

    return questions, examples


# stage     
print('STAGE 1')
soup = makeHttpRequest(base_url + '/java')
stage1 = [div.a['href'] for div in soup.find_all('div', class_='summ')]
# print(len(stage1))

# stage 2
print('STAGE 2')
stage2 = doStage2(stage1)
# print(len(stage2))

# stage 3
print('STAGE 3')
Questions, Examples = doStage3(stage2)

# print("Questions length: ", Questions)
# print("Examples length: ", Examples)

worksheet.write('A1', 'QUESTIONS', bold)
worksheet.write('B1', 'EXAMPLES', bold)

# populate excel sheet
# for row in range(len(Questions)):
#     worksheet.write(row+1,0, Questions[row])

# for row in range(len(Examples)):
#     worksheet.write(row+1,1, Examples[row])


# Populate CSV
row = []
# column1 = []
# column2 = []

row.append(["QUESTIONS", "EXAMPLES"])

# for i in range(len(Questions)):
row.append([Questions[0], Examples[0]])
row.append([Questions[1], Examples[1]])
row.append([Questions[2], Examples[2]])

with open('./csv/cb1.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(row)
