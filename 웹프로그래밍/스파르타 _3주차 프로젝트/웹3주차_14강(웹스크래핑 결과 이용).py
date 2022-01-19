# pymongo로 DB조작하기 - 데이터 find, update 연습하기

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.67xzm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

#1.영화제목 '가버니움'의 평점을 가져와서 , 같은 평점의 영화 제목들을 가져오기

#target_movie = db.movies.find_one({'title':'가버나움'})
#target_star = target_movie['star']
#movies = list(db.movies.find({'star':target_star}))
#for movie  in movies :
    #print(movie['title'])



#2.영화'가버니움'의 평점을 0으로 만들기.

#db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
#cloud.mongodb 가서 데이터 변경됐는지 확인!
