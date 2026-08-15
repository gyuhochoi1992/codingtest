"""
정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ num_list의 길이 ≤ 100
1 ≤ num_list의 원소 ≤ 100
1 ≤ n ≤ 100
"""

def solution(num_list, n):
    return int(n in num_list)

if __name__ == '__main__':
    solution([1, 2, 3, 4, 5], 3)
    solution([15, 98, 23, 2, 15], 20)