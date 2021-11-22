ENGLISH = "en"
KOREAN = "ko"

class Korean:
    def text(self):
        return "안녕하세요"

class English:
    def text(self):
        return "hello world"

class Factory:
    def get_instance(self, language):
        if language == KOREAN:
            return Korean()
        elif language == ENGLISH:
            return English()

class Hello:
    def greeting(self, language):
        ko = Factory().get_instance(language)
        return ko.text()


def main():
    obj = Hello()
    print(obj.greeting(ENGLISH))
    print(obj.greeting(KOREAN))

if __name__ == "__main__":
    main()
