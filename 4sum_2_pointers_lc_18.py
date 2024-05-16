class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums)-1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        ans = []
        for each in result:
            check = False
            for each_a in ans:
                if each == each_a:
                    check = True

            if not check:
                ans.append(each)
        return ans