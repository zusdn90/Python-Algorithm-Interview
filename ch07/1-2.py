"""
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

leetcode: https://leetcode.com/problems/two-sum/

in을 이용한 탐색
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1 :]:
            return [nums.index(n), nums[i + 1 :].index(complement) + (i + 1)]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6

    print(twoSum(nums, target))
