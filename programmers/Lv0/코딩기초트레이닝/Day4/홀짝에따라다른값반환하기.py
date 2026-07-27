# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

def solution(n):
    if n % 2:
        return sum(range(1, n+1, 2))
    return sum([i * i for i in range(2, n+1, 2)])

    """
    answer = 0
    if n % 2 == 0:
        for num in range(1, n+1):
            if num % 2 == 0:
                answer += (num ** 2)
    else:
        for num in range(1, n+1):
            if num % 2 != 0:
                answer += num
    return answer
    """
if __name__ == '__main__':
    solution(7)
    solution(10)