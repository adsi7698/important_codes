class Solution:
    def palindrome(self, val):
        pal_list = []
        while val:
            pal_list.append(val%10)
            val //= 10

        i, j = 0, len(pal_list)-1
        while i <= j:
            if pal_list[i] == pal_list[j]:
                i += 1
                j -= 1
            else:
                return False, len(pal_list)
        return True, 0

    def get_rev(self, val, length):
        result = 0
        while val > 0:
            result += ((val%10)*(10**(length-1)))
            length -= 1
            val //= 10
        return result
    
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = list(set(nums))
        hash_maps_nums = {}
        for each in nums:
            if each not in hash_maps_nums.keys():
                hash_maps_nums[each] = 1

        new_nums = []
        hash_maps_new = {}
        for each in nums:
            if each < 10:
                continue

            check, length = self.palindrome(each)
            if check:
                continue

            rev = self.get_rev(each, length)
            
            while each%10 == 0:
                each //= 10
            
            if rev not in hash_maps_new.keys() and rev not in hash_maps_nums.keys():
                new_nums.append(rev)
                hash_maps_new[rev] = 1
        return len(nums) + len(new_nums)