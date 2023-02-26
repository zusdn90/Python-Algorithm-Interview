"""
투포인터?
2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식을 말한다.
"""

from typing import List


# 문자열 뒤집기
def reverstString(s: List[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)


if __name__ == "__main__":
    input_strs = ["h", "e", "l", "l", "o"]
    reverstString(s=input_strs)
