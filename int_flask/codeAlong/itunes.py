import requests

# term = "Madonna" #can be made to user input

# res = requests.get("https://itunes.apple.com/search", params={'term': term, 'limit': 5})

# data = res.json()

# for result in data['results']:
#     print(result['kind'])
#     print(result['trackName'])

data = {
    'username': 'chickenz',
    'tweets': [
        'hello!', 'goodbye!', 'bock bock', {'id': 1, 'text': 'my first tweet!'}
    ]
}

requests.post('https://eo4z48za1miybwx.m.pipedream.net', json=data)
