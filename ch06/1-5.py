"""
leetcode: https://leetcode.com/problems/reverse-string/
"""

from typing import List


# 문자열 뒤집기
def reverstString(s: List[str]) -> None:
    s.reverse()
    print(s)


if __name__ == "__main__":
    input_strs = ["h", "e", "l", "l", "o"]
    reverstString(s=input_strs)
