import requests
import json

with open('stats.csv', 'w', encoding='utf-8') as f:
    for i in range(1, 6):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}'
        req = requests.get(url)
        data = json.loads(req.text)

        for headline in data:
            _headline = headline['headline']
            _headline = _headline.replace(',', '|')
            f.write(_headline)
            f.write('\n')
