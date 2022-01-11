
# 처음 풀이
def solution(s):
    answer = ""
    number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
              "eight": "8", "nine": "9"};
    index = 0

    while index < len(s):
        if s[index:index + 3] in number:
            answer += number[s[index:index + 3]]
            index += 3
        elif s[index:index + 4] in number:
            answer += number[s[index:index + 4]]
            index += 4
        elif s[index:index + 5] in number:
            answer += number[s[index:index + 5]]
            index += 5
        else:
            answer += s[index]
            index += 1
    return int(answer)


# 간단한 풀이

def solution(s):
    answer = s
    number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
              "eight": "8", "nine": "9"};

    for key, value in number.items():
        answer = answer.replace(key, value)
    return int(answer)