# 여러개의 입력값을 받는 함수
# 몇개를 받을지 정해지지 않았을 때


print('\n ======== 여러개의 인수를 받는 경우 ========')


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result        
    
sum = add_many(1, 2, 3)
print(sum) # 6
print()


sum = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # 55
print(sum)
print()


def add_mul(choice, *args):
    if choice == 'add':
        result = 0 
        for i in args:
            result += i
            
    elif choice == 'mul':
        result = 0
        for i in args:
            result *= i
            
    else:
        result = '없어'
        
    return result

result = add_mul("add", 1, 2, 3, 4, 5)
print(result)


result = add_mul("mul", 1, 2, 3, 4, 5)
print(result)


result = add_mul("div", 1, 2, 3, 4, 5)
print(result)

print('\n======== 키: 벨류를 인수로 받는 경우=======\n')


def print_kwargs(**kwargs):
    print(kwargs)
    

print_kwargs(a=1)
print()


print_kwargs(name='poo', age=3)
print()


print_kwargs(name='홍길동', age=25, city='서울', job='정의로운 도둑')


def create_profile(**info):
    print("===== 프로필 정보 =====")
    for key, value in info.items():
        print(f'{key} : {value}')
        

create_profile(이름='김철수', 나이=30, 직업='개발자', 취미='독서')
print()


data = {'이름' : '콩순이', '나이':'5', '직업':'유치원생', '취미':'놀기'}
create_profile(**data)


print('\n======== 3가지 형식을 인수로 받는 경우=======\n')


def mixed_profile(name, *args, **kwargs):
    print(f'이름 : {name}' )
    print(f'좋아하는 숫자 : {args}')
    print(f'기타 정보 : {kwargs}')
    

mixed_profile('홍길동', 3, 7, 9, age=17, city='서울')
print()


name = '번개맨'
fav_number = [3, 7, 9]
extra_info = {'age' : 15, 'city' : '인천'}

def mix_profile(name, *args, **kwargs):
    print(f'이름 : {name}')
    print(f'좋아하는 숫자 : {args}')
    print("===== 기타 정보 =====")
    for key, value in kwargs.items():
        print(f'{key} : {value}')
    
mix_profile(name, *fav_number, **extra_info)
print()

# 함수의 변환값은 언제나 하나이다


def add_and_mul(a, b):
    return a+b, a*b


result = add_and_mul(3, 4) # (7, 12)
print(result)
print()


result1, result2 = add_and_mul(5, 6)
print(result1) # 11
print(result2) # 30
print()


def add_and_mul(a, b):
    return a+b
    return a*b


result = add_and_mul(2, 3)
print(result)



print('\n======= return의 또 다른 쓰임새 =======\n')


def say_nick(nick):
    if nick == "바보":
        return 
    print(f'나의 별명은 {nick}입니다')
    

say_nick('바보') # 반응 안함
say_nick('천재')


print('\n======= return의 또 다른 쓰임새 =======\n')


def say_myself(name, age, man=True):
    print(f"나의 이름은 {name}입니다")
    print(f"나이는 {age}살 입니다")
    if man : print("남자입니다")
    else : print("여자입니다")
    
    
say_myself('김둘리', 3)
print()
say_myself('김둘리', 3, True)
print()
say_myself('이또치', 3, False)
print()


print('\n======= 지역변수(local), 전역변수(global) =======\n')

a =3

def exam(number):
    a = 0
    a = a + number
    
    
exam(5)

print(a) #3



print('\n======= 반환값으로 받기 =======\n')

a =3

def exam(number):
    a = 0
    a = a + number
    return a
    
print(exam(5))
print(a) #3




print('\n======= global 명령어 사용 =======\n')



a = 3

def exam(number):
    global a 
    a = a + number
    

exam(5)
print(a) # 8



print('\n======= 리스트나 딕셔너리는 함수에서 변경가능 =======\n')


def chage_list(my_list):
    my_list.append(3)
    
    
a = [1, 2, 3]
chage_list(a)

print(a)

print('\n======= 리스트나 딕셔너리는 함수에서 변경가능 =======\n')
def add(a, b):
    """
    두 숫자를 더하는 함수

    parameter
    a (int , float) : 첫 번째 숫자
    b (int , float) : 두 번째 숫자

    return:
    int, float : 두 숫자의 합
    """
    return a + b

print(add.__doc__)
#혹은 
help(add)

print('\n======== 람다식 =========\n')

# 함수를 간단하겜 만들기

def add(a, b):
    return a+b



add2 = lambda a, b : a+b

result = add2(3, 4)
print(result)
print()



distance = lambda x1, y1, x2, y2:((x2-x1)**2 + (y2-y1)**2)**0.5


result = distance(1, 2, 4, 6) #루트{(4-1)제곱 + (6-2)제곱}
print(result) 


print('\n======== 리스트 + 맵 =========\n')


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x**2, numbers))
print(squares) # [1, 4, 9, 16, 25]
print()


print('\n======== 리스트 컴프리헨션 =========\n')


squares2 = [x**2 for x in numbers]
print(squares2)


print('\n======== 리스트 + 필터 =========\n')


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


evens = list(filter(lambda x : x % 2 == 0, numbers2))
print(evens) # [2, 4, 6, 8]
print()


#리스트 컴프리헨션 방식으로 똑같은 작동 구현하기


evens2 = [x for x in numbers2 if x % 2 == 0]
print(evens2)


print("\n======== 예제1 ========\n")


numbers3  = [5, -2, 0, 8, -7]


result = list(map(lambda x : "양수" if x > 0 else('음수' if x < 0 else "0"), numbers3))
print(result)
print()


# 리스트 컴프리헨션 방식으로 똑같은 작동 구현하기


result2 = ["양수" if x > 0 else ("음수" if x < 0 else "0") for x in numbers3]
print(result2)


print('\n======== 예제2 =========\n')
a = [1, 2, 3, 4]

result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]
print()

# 람다 + 맵 + 필터 방식으로 똑같이 구현하기

result3 = list(map(lambda num : num * 3, filter(lambda x : x % 2 == 0, a)))
print(result3)
print()


















