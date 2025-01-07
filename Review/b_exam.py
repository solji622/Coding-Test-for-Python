# 클래스 예제
# Animal 클래스를 만들어 이름과 종류를 저장하고, 소개하는 메서드를 작성

# Animal Class
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def introduce(self):
        print(f"안녕하세요! 저는 {self.type} {self.name} 입니다.")

# 인스턴스 생성
cat = Animal("나비", "고양이")
cat.introduce()