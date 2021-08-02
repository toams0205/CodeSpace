import requests


data = requests.get('http://comic.naver.com/webtoon/weekday.nhn')


list = data.text.split('\n')

num = 1

for line in list:
    print( str(num) +" :" + line)
    num += 1