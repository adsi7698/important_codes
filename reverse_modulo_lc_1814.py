class Solution:
    MODULO = 1_000_000_007

    def reverse(self, val):
        result = 0

        while val:
            temp = val%10
            result = result*10 + temp
            val //= 10
        
        return result

    def countNicePairs(self, nums: List[int]) -> int:
        hash_map = {}
        for each in nums:
            temp = each - self.reverse(each)
            if temp not in hash_map.keys():
                hash_map[temp] = 1
            else:
                hash_map[temp] += 1

        result = 0
        for value in hash_map.values():
            result += ((value * (value - 1)) // 2) % self.MODULO
        return result % self.MODULO