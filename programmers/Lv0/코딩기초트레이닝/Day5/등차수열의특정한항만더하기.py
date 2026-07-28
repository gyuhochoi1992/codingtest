"""
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, d, included):
    print(sum(a + i * d for i, f in enumerate(included) if f))

    """
    answer = 0
    for idx in range(len(included)):
        if included[idx] == True:
            answer += a + (d * idx)
    return answer
    """

if __name__ == "__main__":
    solution(3, 4, [True, False, False, True, True])
    solution(7, 1, [False, False, False, True, False, False, False])