import datetime
import unittest

# 빌더
#     복합 객체의 생성 과정과 표현 방법을 분리하여 동일한 생성 절차에서 서로 다른 표현 결과를 만들 수 있게 하는 패턴이다. 생성자 오버로딩
# 파이썬에 따로 빌더 패턴이 필요하지 않다는 경우가 많아서 예제 소스코드 구하기가 쉽지않아 직접 써본다.


class User:
    id = None
    username = ""
    password = ""

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Post:
    id = None
    user_id = None
    title = ""
    content = ""
    created_at = None

    def __init__(self, id, user_id, title, content, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.created_at = created_at

class Comment:
    id = None
    post_id = None
    content = ""
    created_at = None

    def __init__(self, id, post_id, content, created_at):
        self.id = id
        self.post_id = post_id
        self.content = content
        self.created_at = created_at

class TestCaseSetup:
    users = []
    posts = []
    comments = []

class TestCaseSetupBuilder:
    users = []
    posts = []
    comments = []

    def with_users(self, how_many):
        for i in range(how_many):
            user = User(id=len(self.users)+1, username=str(len(self.users)+1), password=str(len(self.users)+1))
            self.users.append(user)
        return self
    
    def with_posts(self, how_many):
        if not self.users:
            raise Exception
        user_ids = [user.id for user in self.users]
        for i in range(how_many):
            post = Post(id=len(self.posts)+1, title=str(len(self.posts)+1), content=str(len(self.posts)+1), user_id=user_ids[i%len(user_ids)], created_at=datetime.datetime.now())
            self.posts.append(post)
        return self

    def with_comments(self, how_many):
        if not self.posts:
            raise Exception
        post_ids = [post.id for post in self.posts]
        for i in range(how_many):
            comment = Comment(id=len(self.comments)+1, content=str(len(self.comments)+1), post_id=post_ids[i%len(post_ids)], created_at=datetime.datetime.now())
            self.comments.append(comment)
        return self

    def build_test_case(self):
        setup = TestCaseSetup(users = self.user, posts = self.posts, comments = self.comments)
        return setup

class TestCase0(unittest.TestCase):
    def setUp(self):
        TestCaseSetupBuilder().with_users(10).with_posts(20).with_comments(5)
        
    def test_something_0(self):
        pass

    def test_something_1(self):
        pass

class TestCase1(unittest.TestCase):
    def setUp(self):
        pass

    def test_something_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
