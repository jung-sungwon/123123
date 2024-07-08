import hashlib


class Member:
    def __init__(self, name, username, password):
        # 생성자 구현
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        # 메소드 구현
        print(f"Name:{self.name}  ID:{self.username}")


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


def display_members():  # 함수 추가치
    print("--------------------------------------")
    for member in members:
        member.display()  # display 메소드 호출1


def create_post(posts):  # 함수 추가
    # 특정유저가 작성한 게시글의 제목을 모두 프린트 / # 특정 단어가 content에 포함된 게시글의 제목을 모두 프린트
    print("---------------------------------------")
    print(f"특정유저 정성원님이 작성한 게시글의 제목 ")
    for post in posts:
        if post.author == 'a17':
            print(post.title)

    keyword = "특정단어"  # keyword 란 변수 선언
    print("--------------------------------------")
    print(f"게시글 내용에 {keyword}가 포함된 게시글들의 제목 ")
    # for in / if in 으로 post.content 에 keyword("특정 단어")가 들어가 있는 것만 반복문으로 출력
    for post in posts:
        if keyword in post.content:
            print(post.title)


members = []
posts = []


def create_member():
    print("새로운 회원을 등록합니다.")
    name = input("이름을 입력하세요 :")
    username = input("아이디를 입력하세요:")
    password = input("비밀번호를 입력하세요 :")

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    new_member = Member(name, username, password_hash)  # 수정사항 : 해싱된 비밀번호 저장
    members.append(new_member)
    print("회원 등록이 완료되었으며, 비밀번호는 해싱처리되었습니다.")
    print(f"해싱처리된 비밀번호 : {password_hash}")


def create_content():
    print("새로운 게시글을 작성합니다")
    title = input("제목을 입력해주세요 :")
    content = input("내용을 입력해주세요 :")
    username = input("작성자명을 입력해주세요 :")

    new_content = Post(title, content, username)
    posts.append(new_content)


M1 = Member("정성원", "a17", "123123")
M2 = Member("박윤성", "ai8", "231231")
M3 = Member("조준호", "ai9", "312312")
# 3개의 회원 인스턴스

members.append(M1)
members.append(M2)
members.append(M3)

hash1 = hashlib.sha256(M1.password.encode()).hexdigest()
hash2 = hashlib.sha256(M2.password.encode()).hexdigest()
hash3 = hashlib.sha256(M3.password.encode()).hexdigest()
print("기존 비밀번호:", M1.password)
print("SHA-256 Hash :", hash1)
print("기존 비밀번호:", M2.password)
print("SHA-256 Hash :", hash2)
print("기존 비밀번호:", M3.password)
print("SHA-256 Hash :", hash3)


post1 = Post('제목1', '단어', 'a17')
post2 = Post('제목2', '단어', 'a18')
post3 = Post('제목3', '특정단어', 'a19')
posts.append(post1)
posts.append(post2)
posts.append(post3)

post4 = Post('제목4', '단어', 'a17')
post5 = Post('제목5', '단어', 'a18')
post6 = Post('제목6', '특정단어', 'a19')
posts.append(post4)
posts.append(post5)
posts.append(post6)

post7 = Post('제목7', '단어', 'a17')
post8 = Post('제목8', '단어', 'a18')
post9 = Post('제목9', '특정단어', 'a19')
posts.append(post7)
posts.append(post8)
posts.append(post9)

create_member()
create_content()
display_members()
create_post(posts)
