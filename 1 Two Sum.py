class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = [(num, target-num) for num in nums]
        nums_dict = dict(nums_dict)
        for i, n in enumerate(nums):
            try:
                comp = nums_dict[n]
                for j, num in enumerate(nums):
                    if num == comp and i != j:
                        return [i, j]
            except KeyError:
                pass

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []