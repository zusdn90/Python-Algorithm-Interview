"""
로그파일 재정렬

leetcode: https://leetcode.com/problems/reorder-data-in-log-files/
"""
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []

    for log in logs:
        # isdigit으로 숫자,문자 구분
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result = reorderLogFiles(logs=logs)
    print(result)
