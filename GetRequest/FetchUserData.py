import requests

url = "http://localhost:3000/student/1"
##send Get request
response = requests.get(url)
print(response.content)
print(response.status_code)
print(response.headers.get('X-Powered-By'))


