# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num, n):
    return int(num % n == 0)
    """
    if num % n == 0:
        return 1
    else:
        return 0
    """

if __name__ == '__main__':
    solution(98, 2)
    solution(34, 3)
