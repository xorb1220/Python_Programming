# 사용자 정의 모듈
print("start:", __name__)   # 모듈의 이름을 가져오는 내장 변수
PI = 3.1415

def add(a, b):
    return a + b

# 직접 모듈을 실행한 경우에만 입력
if __name__ == "main":
    print(PI)
    print(add(10, 20))
