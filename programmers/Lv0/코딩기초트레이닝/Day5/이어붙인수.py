"""
정수가 담긴 리스트 num_list가 주어집니다.
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    even = int(''.join([str(i) for i in num_list if i % 2 == 0]))
    odd = int(''.join([str(i) for i in num_list if not i % 2 == 0]))
    return even + odd

    """
    odd = ""
    even = ""
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    answer = int(odd) + int(even)
    return answer
    """

if __name__ == '__main__':
    solution([3, 4, 5, 2, 1])
    solution([5, 7, 8, 3])