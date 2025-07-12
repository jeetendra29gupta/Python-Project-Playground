import requests

def app():
    response = requests.get('https://dummyjson.com/quotes/random')
    data = response.json()
    quote = data['quote']
    author = data['author']
    print(f'"{quote}" - By: {author}')

if __name__ == '__main__':
    app()