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
