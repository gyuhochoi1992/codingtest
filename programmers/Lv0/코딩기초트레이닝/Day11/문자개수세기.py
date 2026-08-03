"""
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz']
    """
    answer = [0] * 52
    for c in my_string:
        if 'A' <= c <= 'Z':
            answer[ord(c) - 65] += 1
        elif 'a' <= c <= 'z':
            answer[ord(c) - 97 + 26] += 1
    return answer
    """

if __name__ == '__main__':
    solution("Programmers")