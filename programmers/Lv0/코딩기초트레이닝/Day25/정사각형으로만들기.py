"""
이차원 정수 배열 arr이 매개변수로 주어집니다. arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ arr의 길이 ≤ 100
1 ≤ arr의 원소의 길이 ≤ 100
arr의 모든 원소의 길이는 같습니다.
1 ≤ arr의 원소의 원소 ≤ 1,000
"""

def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    if row_len > col_len:
        diff = row_len - col_len
        for i in range(row_len):
            arr[i].extend([0] * diff)
    elif col_len > row_len:
        diff = col_len - row_len
        for _ in range(diff):
            arr.append([0] * col_len)

    return arr

if __name__ == '__main__':
    solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]])
    solution([[57, 192, 534, 2], [9, 345, 192, 999]])
    solution([[1, 2], [3, 4]])