from bs4 import BeautifulSoup as bs
import requests

url = "https://webscraper.io/test-sites/tables"

response = requests.get(url) # This wil give the html code for the page 
# print(response.status_code)
# print(response.content)

soup = bs(response.content.decode('utf-8'), 'html.parser')
# print(soup)


# # Working with HTML tags
# headings1 = soup.find_all('h1')
# headings2 = soup.find_all('h2')
# images = soup.find_all('img')
# images_src = soup.find_all('img')[0]['src']
# images_alt = soup.find_all('img')[0]['alt']

# print(headings1)
# print(headings2)
# print(images)
# print(images_src)
# print(images_alt)

# Working with tables
table1 = soup.find_all('table')[0]
table2 = soup.find_all('table')[1]
# print(table2)

table_rows = table2.find_all('tr')[1:]
print(table_rows)

last_names = []
for row in table_rows:
    last_name = row.find_all('td')[2].get_text()
    # print(last_name)
    last_names.append(last_name)
    
print(last_names)
    
