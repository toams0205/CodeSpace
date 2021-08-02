import requests


link ='http://i2.ruliweb.com/img/17/07/27/15d837f602e31da04.jpg'

with open('D:\코딩교육\미로게임 맵\1503114759526.jpg', 'wb') as f:
    f.write(requests.get(link).content)

