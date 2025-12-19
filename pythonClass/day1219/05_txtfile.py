# (텍스트) 파일 읽고 쓰기

# r - 읽기 모드 : 파일을 읽기만 할 때 사용한다
# w - 쓰기 모드 : 파일에 내용을 쓸 때 사용한다
# a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다


import os
path = './day1219'

if not os.path.exists(path):
    os.makedirs(path)
    
    
 
print('=======쓰기모드========')   
    
f = open("./day1219/새파일.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data) # 메모장에 쓸 때는 문자열을 넣어야 한다
f.close()

print('=======읽기모드========') 

f = open("./day1219/새파일.txt", 'r', encoding="utf-8")
line = f.readline() # 첫 번째 줄을 반환
print(line)
f.close()


f = open("./day1219/새파일.txt", 'r', encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("./day1219/새파일.txt", 'r', encoding="utf-8")
lines = f.readlines()
print(lines)

for line in lines:
    line = line.strip()
    print(line)

f.close()