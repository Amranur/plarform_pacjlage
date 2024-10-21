import requests

class MyAPIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_data(self, query, categories="general", engines="all", format="json", count=10):
        endpoint = f"{self.base_url}/playground-json"
        params = {
            'query': query,
            'api_key': self.api_key,
            'categories': categories,
            'engines': engines,
            'format': format,
            'count': count,
        }
        headers = {'accept': 'application/json'}
        
        response = requests.get(endpoint, params=params, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Usage:
# client = MyAPIClient('http://36.50.40.36:9000', 'aaa12561-d9a7-4062-9d65-f830e8c9b79c')
# data = client.get_data(query='hi')
# print(data)
