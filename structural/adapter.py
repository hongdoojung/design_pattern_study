# https://ko.wikipedia.org/wiki/%EC%96%B4%EB%8C%91%ED%84%B0_%ED%8C%A8%ED%84%B4

# 오브젝트 어댑터 예시
class Target(object):
    def specific_request(self):
        return 'Hello Adapter Pattern!'

class Adapter(object):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

client = Adapter(Target())
print(client.request())
