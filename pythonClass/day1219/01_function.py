print('\n =========함수=========')

def add(a,b):
    return a + b;

hap = add(3,4) #숫자로 넣어서 변수로 받아서 출력
print(hap)

c = 5
d = 6

hap = add(c,d) # 변수로 넣어서 변수로 받아서 출력하기
print(hap) # 11

print(add(8,9)) # 17

print('\n =========입력값, 반환값 있는 경우=========')

# 조금 더 정석적으로 표현
def add(a,b):
    result = a + b
    return result

hap = add(4,7)
print(hap) # 11

print('\n =========입력값이 없는 함수=========')

def say():
    return 'hi'

say() # 아무것도 안나옴

a = say()
print(a)

def say2():
    print("hi")

say2()

a = say2
print(a)
print(say2)

print('\n =========입력값만 있는 함수=========')

def add2(a,b):
    print(f'{a}와 {b}의 합은 {a+b}입니다.')
    print(f'하지만 반환하는 값은 {a+b}입니다.')
    return a + b
a = add2(3,4)

print(a)


print('\n =========혼합하기=========')

def add2(a,b):
    print(f'{a}와 {b}의 합은 {a+b}입니다.')
    print(f'하지만 반환하는 값은 {a*b}입니다.')
    return a * b

a = add2(3,4)

print(a)

print('\n =========매개변수 지정하여 입력=========')

def sub(a,b):
    return a - b

result = sub(a=3,b =4)
print(result)

result = sub(b = 3,a = 4)
print(result)

def sum(a,b): # 입 o 반 o
    return a + b 

print(sum(4,5)) # 9

def Hi(): # 입 x 반 o
    return 'hi'

a = Hi()
print(a) # hi

def sum2(a,b): # 입 o 반 x
    print(a + b)

sum2(4,5) # 9

def Hi2(): # 입 x 반 x
    print('hi')

Hi2() # hi




