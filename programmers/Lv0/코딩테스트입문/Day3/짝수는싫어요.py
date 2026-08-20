"""
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100
"""
def solution(n):
    return list(range(1, n + 1, 2))

if __name__ == '__main__':
    solution(10)
    solution(15)