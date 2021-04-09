import requests


with open("quotes.csv", 'w', encoding='utf-8') as f:
    for i in range(1, 11):
        url = f'https://quotes.toscrape.com/page/{i}'
        r = requests.get(url)
        html = r.text

        print('Page:', i)
        quote = ""
        author = ""
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">', '').replace('</span>', '')
                quote = line.strip()

            elif '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
                author = line.strip()

                f.write(author + ", " + quote)
                f.write("\n")


