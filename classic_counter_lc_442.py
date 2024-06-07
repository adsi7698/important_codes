class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        checker = [False]*(max(nums)+1)
        result = []
        for each in nums:
            if checker[each]:
                result.append(each)
            else:
                checker[each] = True

        return result