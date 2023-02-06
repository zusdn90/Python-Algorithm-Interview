def is_palindrome(s: str) -> bool:
    strs = []

    for char in s:
        # 영문자, 숫자 여부 판별
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


if __name__ == "__main__":
    import time

    start = time.time()

    test_str = "nans"
    print(is_palindrome(test_str))
    print(f"{time.time()-start:.6f} sec")