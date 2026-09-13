class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # in this problem we have to iterate both part of the array, index and value, beacuse we have to return the index, but the value is important 
        hash = { }
        for i, v in enumerate(nums):
            findValue = target - v
            if findValue in hash:
                return [hash[findValue],i]
            hash[v] = i