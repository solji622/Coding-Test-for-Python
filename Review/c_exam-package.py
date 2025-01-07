from pprint import pprint
import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

# 1. 미세먼지 수치가 60미만인 구만 출력하기
for i in gus:
    if (i['IDEX_MVL'] < 60) :
        pprint(rjson)


# 2. 구 이름을 받아 미세먼지 수치를 리턴하는 함수
def get_gu_mise(gu):
    get_mvl = 0
    for i in gus:
        if i['MSRSTE_NM'] == gu:
            get_mvl = i['IDEX_MVL']
            return get_mvl
    print("미세먼지 수치가 없습니다.")
    return ""

print(get_gu_mise("중구"))
print(get_gu_mise("종로구"))
print(get_gu_mise("중원구"))  # 서울에 없는 구