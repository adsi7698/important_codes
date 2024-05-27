class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = 0
        ncr = 1
        length = len(nums)-1

        for i, num in enumerate(nums):
            result = (result + num * ncr)%10
            ncr = (ncr * (length-i) // (i+1))

        return result