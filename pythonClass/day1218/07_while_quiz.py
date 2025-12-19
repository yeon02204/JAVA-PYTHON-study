print('\n======= while문 =======')


'''
while 조건식:
    실행할 코드

조건식이 True인 동안 반복 실행
조건이 False가 되면 반복 종료
'''


print('\n======= 예제 1 =======\n')

i = 1

while i <= 5:
    print(i)
    i += 1




print('\n======= 예제 2 =======\n')


sleep = 0 
i = 0

while sleep < 10:
    sleep = sleep + 1
    i = i + 1
    print(f"잠을 {sleep}시간째 자고 있습니다.")
    print(f"도둑이 {i}회 들었습니다.")
    if sleep == 10:
        print("잡았다 요놈!!!")





print('\n======= 예제 3 =======\n')


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """



number = 0
while number != 4:
    print(prompt)
    number = int(input())





# ======= 로또 생성 =======
# while, random.randint, set 사용

import random

lotto_numbers = set()  # 빈 집합 생성
while len(lotto_numbers) < 6:
    number = random.randint(1, 45)  # 1~45 사이 랜덤 숫자
    lotto_numbers.add(number)        # 집합에 추가 (중복 자동 제거)

print(lotto_numbers)

coffee = 5
money = 300
while money:
    print("돈을 받았으니 커피를 준다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다")
        break
    
coffee = 10
while False:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피 드세요")
        coffee -= 1
        print("남은 커피 : ",coffee, "개")
    elif money > 300:
        print("커피 드세요, 잔돈은 : ", money-300, "원")
        coffee -= 1
        print("남은 커피 : ",coffee, "개")
    else:
        print("돈이 부족합니다")
        print("남은 커피 :", coffee,"개")
    if coffee == 0:
        print("커피가 없어서 자판기 종료")
        break

print("\n======= continue =======")    
# while 문의 맨 처음으로 돌아간다

a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

print("\n======= 무한루프 =======")    
#무한 루프 탈출은 Ctrl + c 혹은 터미널창 닫기
i = 11
while i < 10:
    print("야호")
    
    
print("\n======= while else =======")
count = 0
while count < 3:
    print(f"카운트 : {count}")
    count += 1
else:
    print("while 문이 정상 종료 되었습니다")

    
print("\n======= while else =======")
count = 0
while count < 5:
    if count == 2:
        break
    print(f"카운트 : {count}")
    count += 1
else:
    print("while 문이 정상 종료 되었습니다")
    
print("\n======= 중첩 while문 =======")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1 
