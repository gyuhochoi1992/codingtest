"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 <numer1, denom1, numer2, denom2 < 1,000
"""

import math
# from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(numer, denom)
    return [numer // gcd, denom //gcd]

    """
    ans = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [ans.numerator, ans.denominator]
    """

if __name__ == '__main__':
    solution(1, 2, 3, 4)
    solution(9, 2, 1, 3)