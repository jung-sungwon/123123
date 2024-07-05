print(1)


class Member:
    def __init__(self, name, username, password):
        # 생성자 구현
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"Name:{self.name}  ID:{self.username}")


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


def display_members():  # 함수 추가
    print("--------------------------------------")
    for member in members:
        member.display()  # display 메소드 호출


members = []

member1 = Member("정성원", "ai7", "123123")
member2 = Member("장성원", "ai8", "231231")
member3 = Member("종성원", "ai9", "312312")

members.append(member1)
members.append(member2)
members.append(member3)

display_members()
