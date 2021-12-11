# 프록시 패턴(proxy pattern)은 컴퓨터 프로그래밍에서 소프트웨어 디자인 패턴의 하나이다.
# 일반적으로 프록시는 다른 무언가와 이어지는 인터페이스의 역할을 하는 클래스이다. 프록시는 어떠한 것(이를테면 네트워크 연결, 메모리 안의 커다란 객체, 파일, 또 복제할 수 없거나 수요가 많은 리소스)과도 인터페이스의 역할을 수행할 수 있다.
# 리얼 이미지와 프록시 이미지 예시

class SubjectInterface:
    def add(self, a, b):
        pass

    def sub(self, a, b):
        pass

class RealSubject(SubjectInterface):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

class ProxyClass(SubjectInterface):
    def __init__(self):
        self.subject = RealSubject()

    def add(self, a, b):
        return self.subject.add(a, b)

    def sub(self, a, b):
        return self.subject.sub(a, b)

if __name__ == "__main__":
    p = ProxyClass()
    print(p.add(100, 25)) # 125
    print(p.sub(100, 25)) # 75
