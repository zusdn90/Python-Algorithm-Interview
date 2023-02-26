"""
팰린드롬?
앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 말함.
"""


# deque 활용
def is_palindrome(s: str) -> bool:
    import re

    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]  # slicing


if __name__ == "__main__":
    import time

    start = time.time()

    test_str = "nans"
    print(is_palindrome(test_str))
    print(f"{time.time()-start:.6f} sec")
