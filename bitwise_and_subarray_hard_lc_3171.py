class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = float('inf')

        and_results = []

        for each in nums:
            temp_and = [each]

            for and_result in and_results:
                updated_and = and_result & each
                if updated_and not in temp_and:
                    temp_and.append(updated_and)

            and_results = temp_and

            for and_result in and_results:
                result = min(result, abs(and_result - k))

                if result == 0:
                    return result

        return result