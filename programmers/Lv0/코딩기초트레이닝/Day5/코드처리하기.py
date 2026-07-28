"""
문자열 code가 주어집니다.
code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.
"""
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
    """
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != str(1):
                if idx % 2 == 0:
                    answer += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != str(1):
                if idx % 2 != 0:
                    answer += code[idx]
            else:
                mode = 0
    if answer == "":
        answer = "EMPTY"
    return answer
    """
if __name__ == "__main__":
    solution("abc1abc1abc")