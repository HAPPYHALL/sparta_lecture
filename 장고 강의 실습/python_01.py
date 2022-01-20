
#문자열을 기준으로 나누기
a = "love, eat, coding"
split_result = a.split(',')
print(split_result)

#리스트 인덱스
my_fav = ['python','love','coding']
print(my_fav[0])
print(my_fav[1])
print(my_fav[2])

#리스트 인덱스+ 추가하기
my_fav.append('paul')
my_fav.append('python')
print(my_fav)


# key:value 형태의 딕셔너리
# 콜론(:) 을 기준으로 왼쪽이 '키' 오른쪽이 키에 대응하는 '값'이라고 생각 하면 됩니다!
my_player = {'name':'손흥민'}
print(my_player)


#딕셔너리 값 가져오기  .get()형식은 장고에서 쓰이는 방법
my_info = {'name':'paul','number':'01012345678','birth':'0714'}
print(my_info)
print(my_info['name'])
print(my_info.get('name'))


#조건문
my_age = 10

if my_age == 100:
    print("저는 100살입니다.")
else :
    print("거짓말!!!")


#반복문
jumsu_list = [90, 100, 25, 35, 40]

for jumsu in jumsu_list:
    print(jumsu)


