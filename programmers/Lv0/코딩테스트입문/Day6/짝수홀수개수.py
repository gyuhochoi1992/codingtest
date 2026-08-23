"""
정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ num_list의 길이 ≤ 100
0 ≤ num_list의 원소 ≤ 1,000
"""
def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    return answer

if __name__ == '__main__':
    solution([1, 2, 3, 4, 5])
    solution([1, 3, 5, 7])