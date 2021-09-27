import requests

URL = 'http://localhost:9002/graphql'

query_document = '''
{
  allIngredients {
    name
  }
}
'''

result = requests.get(URL, params={'query': query_document})

print(result.json())
