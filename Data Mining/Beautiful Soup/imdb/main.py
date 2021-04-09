import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.find_all('tr')

for tr in trs:
    name_td = tr.find('td', {'class': 'titleColumn'})
    rating_td = tr.find('td', {'class': 'ratingColumn'})

    movie_id = name_td.a['href']
    movie_url = f'https://www.imdb.com/{movie_id}'
    movie_page = requests.get(movie_url).text
    movie_soup = BeautifulSoup(movie_page, 'html.parser')

    info = movie_soup.find('div', {'class': 'subtext'})
    a = info.findAll('a')

    print(name_td.a.string)
    print(info.time.string.strip())
    print(a[0].string.strip())
    print(a[1].string.strip())
    print('------------------')