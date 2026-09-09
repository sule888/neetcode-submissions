class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, n in enumerate(nums):
            res = target - n 
            if res in h_map:
                return [h_map[res],i ]
            h_map[n] = i