# 포맷팅
# 포맷팅 = 데이터의 값은 그대로 두고, 표현 방식만 바꾸는 것
# 사람이 읽기 좋게(가독성)
# 시스템 간 형식을 맞추기 위해

# 언제부터 쓰였나
# "출력"이 생긴 순간부터 필수 개념
# 이후 모든 언어에 기본 탑재

# C언어 : printf
# Java : String.format, printf
# Python : %, format(), f-String
# JS : 템플릿 리터럴
# SQL : FORMAT()


# =============================================================

# 문제 1번
# 정수 age = 20이 있다
# 다음과 같이 출력하시오 
# 나이 : 20

# 문제 2번
# 이름(name = "홍길동")과 점수(score = 90)가 있다
# 다음과 같이 출력하시오
# 이름 : 홍길동, 점수 : 90

# 문제 3번(실무 많이 사용) 
# 실수 pi = 3.141592를 소수점 둘째 자리까지 출력하시오

# 문제 4번
# user_id = "Kim", age = 25일때 다음 정보로 로그 메시지를 만드시오
# [INFO] userId = kim, age = 25

# 문제 5번(실무 많이 사용) 
# money = 123456789
# 123,456,789 형태로 출력하려면 f-String를 어떻게 작성해야 하는가

# 문제 6번(실무 많이 사용)
# datetime 객체가 아래와 같이 주어졌을 때
# 출력 결과가 2025/03/15 14:30이 되도록 f-string 포맷을 작성하시오

from datetime import datetime
now = datetime(2025, 3, 15, 14, 30, 5)
print(f"{now:%Y/%m/%d %H:%M}")

# print() 안에 f-String 작성
print()

# 함수를 호출할 수 없는 경우
# 1) return 없는 함수
# def print_hello():
#     print("hello")

# print(f"result={print_hello()}")

# 문제 7번 
# 아래 가격이 출력되도록 작성하시오
price =9876543.219
tax_rate =0.1

print()
print()
print()

# 가격: 9,876,543.22원
# 세금: 987,654.32원
# 총액: 10,864,197.54원

# 문제 8번
# 아래 답이 출력되도록 정렬을 사용해서 공백포함 전체폭 8칸이 되도록 채워라
value = 12.3
print() 
# |    12.3|

# 문제 8번
# (1) 텍스트 왼쪽 + 숫자 오른쪽
# 아래 답이 출력되도록 name 왼쪽 정렬 전체폭 10칸 sales는 오른쪽 정렬 총 12칸을 채우고 
# sales의 소숫점 둘째자리까지 반환하라 그리고 천단위로 ,가 삽입되게 출력하라
name = "kim"
sales = 12900000.5
print()
# |kim       |12,900,000.50|

# 문제 9번 
# (2) 퍼센트 정렬
# 아래 답이 출력되도록 rate 오른쪽 정렬 전체폭 8칸을 채워라
# rate의 소숫점 둘째 자리까지 반환하라 
rate = 0.7325
print()  
# |  73.25%|

# 문제 11번
# 아래 값이 출력되도록 작성해라
def get_status(age):
    return "adult" if age >= 20 else "minor"

age = 23
print()
# status=adult 
 
# 문제 12번
# 아래 calc_total 값이 출력되도록 작성해라
def calc_total(price, count):
    return price * count

print()
# total = 3000원

# 문제 13번
# len() — 길이 / 개수 출력
items = [1, 2, 3, 4]
print()
# item의 문자열 개수를 구해라
 
# 문제 14번
# sum() - 합계 구하기
# sum()을 사용하여 price의 합계를 구해라
prices = [1200, 800, 450]
print()
 
# 문제 15번
# price값을 더하여 출력하시오
prices = [1200, 35000, 780]

def total(xs):
    return sum(xs)

print()
# (정렬 + 함수 호출 + 콤마) 

# 문제 16번
# score 아래의 값이 출력되도록 빈칸을 작성하세요
scores = [70, 80, 90, 100]

avg = sum(scores) / len(scores)

print()
# (평균 + 소수점 + 길이 계산)

# 문제 17번
# 아래처럼 출력되도록 작성하시오
def grade(score):
    return "PASS" if score >= 60 else "FAIL"

score = 58

print()
# |RESULT|  FAIL|       




















