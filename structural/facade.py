# 사드(프랑스어: façade[fəˈsɑːd] 영어: facade) 패턴(외관 패턴)은 소프트웨어 공학 디자인 패턴 중 하나이다. 객체 지향 프로그래밍 분야에서 자주 쓰인다. Facade (외관)는 "건물의 정면"을 의미한다.

# 퍼사드는 클래스 라이브러리 같은 어떤 소프트웨어의 다른 커다란 코드 부분에 대한 간략화된 인터페이스를 제공하는 객체이다.

# 퍼사드는 소프트웨어 라이브러리를 쉽게 사용할 수 있게 해준다. 또한 퍼사드는 소프트웨어 라이브러리를 쉽게 이해할 수 있게 해 준다. 퍼사드는 공통적인 작업에 대해 간편한 메소드들을 제공해준다.
# 퍼사드는 라이브러리를 사용하는 코드들을 좀 더 읽기 쉽게 해준다.
# 퍼사드는 라이브러리 바깥쪽의 코드가 라이브러리의 안쪽 코드에 의존하는 일을 감소시켜준다. 대부분의 바깥쪽의 코드가 퍼사드를 이용하기 때문에 시스템을 개발하는 데 있어 유연성이 향상된다.
# 퍼사드는 좋게 작성되지 않은 API의 집합을 하나의 좋게 작성된 API로 감싸준다.
# 래퍼(wrapper)가 특정 인터페이스를 준수해야 하며, 폴리모픽 기능을 지원해야 할 경우에는 어댑터 패턴을 쓴다. 단지, 쉽고 단순한 인터페이스를 이용하고 싶을 경우에는 퍼사드를 쓴다
# 관리자를 통한 결혼식 예약 예시
