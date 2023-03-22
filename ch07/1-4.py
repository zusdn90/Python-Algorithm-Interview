"""
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

leetcode: https://leetcode.com/problems/two-sum/

조회 구조 개선
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6

    print(twoSum(nums, target))
