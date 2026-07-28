# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    s = sum(num_list)**2
    m = eval('*'.join([str(n) for n in num_list]))
    return 1 if s > m else 0
    """
    num1 = sum(num_list)**2
    num2 = 1
    for i in num_list:
        num2 *= i
    if num1 > num2:
        return 1
    else:
        return 0
    """
if __name__ == "__main__":
    solution([3, 4, 5, 2, 1])
    solution([5, 7, 8, 3])