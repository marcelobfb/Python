import requests

resp=requests.get('https://g1.globo.com')
print('Status code:',resp.status_code)
print('↓↓Header↓↓')
print(resp.headers)
print('\n\033[32m↓↓Content↓↓\033[m')
print(resp.content)