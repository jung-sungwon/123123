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

posts = []

post1 = Post('이무진', '신호등', 'member1.name')
post2 = Post('다이나믹듀오', '고백', 'member1.name')
post3 = Post('livingston', 'shadow', 'member1.name')
posts.append(post1)
posts.append(post2)
posts.append(post3)

post4 = Post('livingston', 'architect', 'member2.name')
post5 = Post('livingston','neon', 'member2.name')
post6 = Post('benson boone','beautifil things', 'member2.name')
posts.append(post4)
posts.append(post5)
posts.append(post6)

post7 = Post('christopher', 'bad', 'member3.name')
post8 = Post('bruno mars','when i was your man', 'member3.name')
post9 = Post('charlie puth','dangerously', 'member3.name')
posts.append(post7)
posts.append(post8)
posts.append(post9)

print(posts)


