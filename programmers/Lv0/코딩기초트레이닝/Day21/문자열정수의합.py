"""
한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ num_str ≤ 100
"""

def solution(num_str):
    return sum([int(s) for s in num_str])

if __name__ == '__main__':
    solution("123456789")
    solution("1000000")