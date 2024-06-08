class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        count = 0
        for i in nums:
            if i < pivot:
                result.append(i)
            elif i == pivot:
                count += 1

        for i in range(count):
            result.append(pivot)
        
        for i in nums:
            if i > pivot:
                result.append(i)
        return result