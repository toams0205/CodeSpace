import requests
from bs4 import BeautifulSoup
from os.path  import basename

data = requests.get('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue')


content = BeautifulSoup(data.text,'html.parser')



titles = content.find_all("td", attrs={'class':'title'})

host ='http://comic.naver.com'


for title in titles:
    link = title.a['href']
    print(link)
    print(title.text)

