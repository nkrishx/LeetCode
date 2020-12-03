class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, number in enumerate(nums):
            val = target - number
            if val not in dic:
                dic[number] = index
            else:
                return [index,dic[val]]
