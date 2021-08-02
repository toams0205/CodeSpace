import requests
import json

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = '2f86d49168224127abd508fc3e682be2'
headers['Content-Type'] = 'application/octet-stream'


bytes = open('사진', 'rb').read()
data = bytes
params = None

_url =""

try:
    response  = requests.request('post', _url,  data=data, headers=headers, params=params)
    result = response.content

    result = json.loads(result)

    print(result)

    scores = result[0]['scores']

    for score in scores.items():
        print(score[0])
        print(score[1])
        print("--------------------")

except Exception as e:
    print("error ")
    print(e)
