import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient             #####   DB 할 시에만, 3줄 작성!!!!!!!!!!!!!!
client = MongoClient('mongodb+srv://test:sparta@cluster0.67xzm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta    #############여기까지

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)  #내가 전체 데이터 불러오려고 하는 인터넷 주소 복붙! EX)네이버 영화, 지니 사이트

soup = BeautifulSoup(data.text, 'html.parser')  #soup 맨 위에서 여기까지가 크롤릴 기본 준비!!!!!!!!!!!!!!!!!!! 복붙!

# = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
#print(title.text) -> select_one으로 '밥정'이라는 결과값만 나오게 할 수 있다는 것!

movies = soup.select('#old_content > table > tbody > tr')

## movies (tr들) 의 반복문을 돌리기
for movie in movies:
    a = movie.select_one('td.title > div > a')

    #if a != None :   -> 밑에 구문과 같은 뜻. a가 none이 아닐 때
    if a is not None :
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = a.text
        star = movie.select_one('td.point').text

        # 저장 - 예시 (양식)
        #doc = {'name': 'bobby', 'age': 21}
        #db.users.insert_one(doc)
        doc = {
            'title': title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc) #movies 파일에 새로이 만들어서 집어넣음음