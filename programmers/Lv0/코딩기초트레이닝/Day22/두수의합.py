"""
0 이상의 두 정수가 문자열 a, b로 주어질 때, a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ a의 길이 ≤ 100,000
1 ≤ b의 길이 ≤ 100,000
a와 b는 숫자로만 이루어져 있습니다.
a와 b는 정수 0이 아니라면 0으로 시작하지 않습니다.
"""
def solution(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    res = []

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        res.append(str(total % 10))
        carry = total // 10

    return "".join(reversed(res))

if __name__ == '__main__':
    solution("582", "734")
    #solution("18446744073709551615", "287346502836570928366")
    #solution("0", "0")