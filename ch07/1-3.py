"""
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

leetcode: https://leetcode.com/problems/two-sum/

첫번째 수를 뺀 결과 키 조회
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6

    print(twoSum(nums, target))
