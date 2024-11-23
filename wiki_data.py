from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url)

soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

get_table = soup.find(class_='wikitable')

mutable = []
immutable = []

table_rows = get_table.find_all('tr')[1:]


for row in table_rows:
    code = row.find_all('td')[1].get_text(strip=True)
    code2 = row.find_all('td')[0].get_text(strip=True)
    
    if code == 'mutable':
        mutable.append(code2)
    else:
        immutable.append(code2)


print(f'Mutable: {mutable}\n')
print(f'Immutable: {immutable}')


