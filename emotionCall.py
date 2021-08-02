import requests


headers = dict()
headers['Ocp-Apim-Subscription-Key'] = '2f86d49168224127abd508fc3e682be2'
headers['Content-Type'] = 'application/json'


urlImage = ''
json = { 'url': urlImage }
data = None
params = None

_url ="https://api.projectoxford.ai/emotion/v1.0/recognize"

try:
    response  = requests.request('post', _url, json=json, data=data, headers=headers, params=params)
    result = response.content

    print(result)

except Exception as e:
    print("error ")
    print(e)
