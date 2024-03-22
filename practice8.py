# Python에서 제공하는 몇가지의 숫자처리 함수

print(abs(-5)) # absolute(절댓값처리기호)에 따라 5
print(pow(4, 2)) # power(x의 y승으로 처리해주는 기호)에 따라 16
print(max(5, 12)) # max(최댓값 출력 기호)에 따라 12
print(min(5, 12)) # min(최솟값 출력 기호)에 따라 5
print(round(3.14)) # round(반올림 출력 기호)에 따라 3
print(round(4.99)) # 5

'''
Python에서 제공하는 MathLibrary를 활용하는 방법
(이후에 배우게 될테니 간단히 느낌만 잡을것)
'''

from math import * # mathlibrary내의 모든함수들을 이용하겠다는 의미
print(floor(4.99)) #floor(내림 출력 기호)에 따라 4
print(ceil(3.14)) # ceiling(올림 출력 기호)에 따라 4
print(sqrt(16)) # sqrt(제곱근 출력 기호)에 따라 4
