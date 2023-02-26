"""
가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
leetcode: https://leetcode.com/problems/most-common-word/
"""

import re
import collections
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # 정규식에서 \w는 단어 문자를 뜻하며, ^은 not을 의미한다.
    # 단어 문자가 아니면 공백으로 치환
    words = [
        word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned
    ]

    counts = collections.Counter(words)
    print(counts)

    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    result = mostCommonWord(paragraph=paragraph, banned=banned)
    print(result)
