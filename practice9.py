# 랜덤함수이자 난수. 즉, 숫자를 무작위로 뽑아주는 함수를 의미함.

from random import *

print(random()) # 0.0 ~ 1.0 미만의 값을 생성하라는 의미
print(random() * 10) # 0.0 ~ 10.0 미만의 값을 생성하라는 의미
print(int(random() * 10)) # int는 정수형을 의미하는 함수이므로 소수점 뒤의 자리가 생략됨
print(int(random() * 10))
print(int(random() * 10)) # 0 ~ 10 미만의 값을 생성 

print(int(random() * 10) + 1) # 0을 제외한 10이하의 값을 생성하고 싶을때
'''
왜 위 수식[print(int(random() * 10) + 1)]은 10미만이 아닌 '이하'일까? 
: int(random())값 전체에 1을 더하는 수식꼴이기에
0 ~ 9까지 돌아가던 함수가 1 ~ 10까지로 영역이 바뀌게 되었기 때문.
'''

# 로또값 출력(로또는 1 ~ 45까지의 수 중 랜덤한 값이 나옴)

print(int(random() * 45) + 1) # 1 ~ 45 이하의 값을 생성
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

# 위 수식을 표현하는 다양한 방법(가시성 향상)
print(randrange(1, 45)) # 1 ~ 45 미만의 값을 생성
print(randrange(1, 45))
print(randrange(1, 45))
print(randrange(1, 45))
print(randrange(1, 45))
print(randrange(1, 45))

print(randint(1, 45)) # 1 ~ 45 이하의 값을 생성
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
