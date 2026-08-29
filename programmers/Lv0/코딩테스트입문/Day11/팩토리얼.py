"""
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

i! ≤ n
제한사항
0 < n ≤ 3,628,800
"""
import math

def solution(n):
    for i in range(10, 0, -1):
        if n >= math.factorial(i):
            return i

    """
    factorial = 1
    i = 1
    while factorial * (i + 1) <= n:
        i += 1
        factorial *= i
    return i
    """

if __name__ == '__main__':
    solution(3628800)
    solution(7)