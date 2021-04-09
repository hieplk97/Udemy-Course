import requests
import json

with open('news.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 6):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}'
        req = requests.get(url)
        data = json.loads(req.text)

        for news in data:
            f.write(news['author'] + ' | ' + news['summary'])
            f.write('\n')
