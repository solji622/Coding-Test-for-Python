# A. 과일 갯수 세기
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# 1. 리스트에서 사과의 갯수 세기
cnt = 0
for i in fruits :
    if i == '사과' :
        cnt += 1
print(cnt)
print("")

# 2. 함수 만들어서 특정 과일 입력 시 해당 과일 갯수 리턴
def count_fruits(fruit) :
    cnt = 0
    for i in fruits:
        if i == fruit:
            cnt += 1
    return cnt

subak_count = count_fruits('수박')
print(subak_count) #수박의 갯수

gam_count = count_fruits('감')
print(gam_count) #감의 갯수

print()



# B. 딕셔너리 응용
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

# 1. 모든 사람의 이름과 나이 출력
for i in people :
    print(i)

# 2. 이름을 받으면 age 리턴해주는 함수 작성
def get_age(name):
    age = 0
    for i in people :
        if i['name'] == name :
            age = i['age']
    return age

print(get_age('bob'))
print(get_age('kay'))

