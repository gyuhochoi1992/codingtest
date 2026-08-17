"""
양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ n ≤ 30
"""

def solution(n):
    answer = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    dir_idx = 0

    for num in range(1, n * n + 1):
        answer[x][y] = num

        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            dir_idx = (dir_idx + 1) % 4
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]

        x, y = nx, ny

    return answer

if __name__ == '__main__':
    solution(4)
    solution(5)