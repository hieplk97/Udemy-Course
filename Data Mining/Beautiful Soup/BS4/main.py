from bs4 import BeautifulSoup
import requests

url = f'https://quotes.toscrape.com/'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

'''
print(soup.title)
print(soup.title.string)
print(soup.title.parent)
print(soup.title.parent.name)
for tag in soup.find_all('a'):
    print(tag)
'''

with open('bs4_quotes.txt', 'w', encoding='utf-8') as f:
    for tag in soup.find_all('span', {'class': 'text'}):
        f.write(tag.string)
        f.write('\n')
