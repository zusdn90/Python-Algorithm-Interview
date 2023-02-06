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
