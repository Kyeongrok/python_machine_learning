# 핵심 로직 2의 배수, 3의 배수 ... 7의 배수를 모두 지웁니다
from math import sqrt

def solution(n):

    ns = list(range(2, n + 1))

    print(ns)

    for i in range(int(sqrt(n))):
        print(i)

    return []

solution(100)
