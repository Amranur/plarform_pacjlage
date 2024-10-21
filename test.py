from api_client import MyAPIClient

client = MyAPIClient('http://36.50.40.36:9000', 'aaa12561-d9a7-4062-9d65-f830e8c9b79c')
data = client.get_data(query='hi')
print(data)
