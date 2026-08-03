"""
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
"""

def solution(n, k):
    return list(range(k, n + 1, k))
    """
    answer = []
    for num in range(1, n + 1):
        if num % k == 0:
            answer.append(num)
    return answer
    """

if __name__ == '__main__':
    solution(10, 3)
    solution(15, 5)