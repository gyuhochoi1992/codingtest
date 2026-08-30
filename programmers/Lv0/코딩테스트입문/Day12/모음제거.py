"""
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
my_string은 소문자와 공백으로 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
"""
def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels:
        my_string = my_string.replace(v, '')
    return my_string

    """
    return ''.join([c for c in my_string if c not in "aeiou"])
    """

if __name__ == '__main__':
    solution("bus")
    solution("nice to meet you")