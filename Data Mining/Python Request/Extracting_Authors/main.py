import requests

r = requests.get('https://quotes.toscrape.com/')
print(r.status_code)

html = r.text

with open('authors.txt', 'w') as f:
    for line in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
            line = line.strip()

            print(line)
            f.write(line)
            f.write('\n')
