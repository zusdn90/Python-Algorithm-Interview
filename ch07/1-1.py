"""
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

leetcode: https://leetcode.com/problems/two-sum/

브루트 포스 풀이
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))
