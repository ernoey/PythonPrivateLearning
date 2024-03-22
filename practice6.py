# 기본 산술연산자와 기타 부호연산자
# 출력값과 Boolean연산자 정리
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 = 8
print(5%3) # 5/3의 나머지 2
print(10%3) # 10/3의 나머지 1
print(5//3) # 5/3의 몫 1
print(10//3) # 10/3의 몫 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # ==은 똑같다는 의미. 고로 True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3 ) # True
print(not (1 != 3)) #False

# and 연산자
print((3 > 0) and (3 < 5)) # True. 두 기호 모두 성립하면 True
print((3 > 0) & (3 < 5)) # True (and 기호)

print((3 > 0) or (3 > 5)) # True. 둘 중 하나의 조건만 성립해도 True
print((3 > 0) | (3 > 5)) # True (or 기호)

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False