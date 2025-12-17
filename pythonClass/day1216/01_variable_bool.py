#=========1번 문제=========
#bool 자료형과 비교 연산
"""
다음 코드를 실행했을 때,
 변수 result에 저장되는 최종 불(Boolean)의 타입을 제출하시오.
A = 2
B = 1
result = (A < B)
"""

print("----------1번-----------")
A = 2
B = 1
result = (A < B)

print(result) # False


#=========2번 문제=========
#변수의 할당과 재사용
"""
다음 코드를 실행했을 때, 변수 sum_val의 최종 값을 제출하시오.
num1 = 10
num2 = 20
sum_val = num1 + num2
"""

print("----------2번-----------")
num1 = 10
num2 = 20
sum_val = num1 + num2

print(sum_val) # 30



#=========3번 문제=========
#type 함수를 이용한 자료형 확인
"""
다음 코드를 실행했을 때,
변수 type_info에 저장되는 최종 값을 제출하시오.
is_check = True
type_info = type(is_check)
"""
print("----------3번-----------")
is_check = True
type_info = type(is_check)
print(type_info) # <class 'bool'>


#=========4번 문제=========
#자료형의 참/거짓 판별 (Truthy/Falsey)
"""
다음 코드를 실행했을 때, 
print() 함수를 통해 출력되는 최종 불 값을 제출하시오.
data_list = [1, 2, 3]
print(bool(data_list))
"""
print("----------4번-----------")
data_list = [1, 2, 3]
print(bool(data_list)) # True


#=========5번 문제=========
#빈 자료형의 참/거짓 판별 (Falsey)
"""
다음 코드를 실행했을 때, 
print() 함수를 통해 출력되는 최종 불 값을 제출하시오.
data_dict = {}
print(bool(data_dict))
"""
print("----------5번-----------")
data_dict = {}
print(bool(data_dict)) #False


#=========6번 문제=========
#not 논리 연산자 사용
"""
다음 코드를 실행했을 때,
 변수 is_allowed에 저장되는 최종 불 값을 제출하시오.
 is_locked = True
is_allowed = not is_locked
"""
print("----------6번-----------")
is_locked = True
is_allowed = not is_locked

print(is_allowed) # False


#=========7번 문제=========
#변수의 재할당
"""
다음 코드를 실행했을 때,
 변수 count의 최종 값을 제출하시오.
 count = 5
count = count + 2
count = count - 1
"""

print("----------7번-----------")
count = 5
count = count + 2
count = count - 1

print(count) # 6




#=========8번 문제=========
#복합 논리 연산 (and, or)
"""
다음 코드를 실행했을 때,
 변수 access에 저장되는 최종 불 값을 제출하시오.
 key = True
day = False
vip = False

access = (key and day) or vip
"""

print("----------8번-----------")

key = True
day = False
vip = False

access = (key and day) or vip

print(access) # False



#=========9번 문제=========
#리스트 복사 ([:] 사용)
"""
다음 코드를 실행했을 때, 변수 b의 최종 리스트 값을 제출하시오.
a = [10, 20]
b = a[:]
a[0] = 50
"""
print("----------9번-----------")
a = [10, 20]
b = a[:]
a[0] = 50

print("b :",b) # b : [50,20]



#=========10번 문제=========
#다중 변수 값 교환
"""
다음 코드를 실행했을 때, 변수 x의 최종 값을 제출하시오.
x = 'apple'
y = 'banana'
z = 'kiwi'

x, y, z = z, y, x
"""

print("----------10번-----------")

x = 'apple'
y = 'banana'
z = 'kiwi'

x, y, z = z, y, x

print(x) # Kiwi