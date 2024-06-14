class Solution:
    def get_parents(self, val):
        if val == 1:
            return 0
        return (val-2) // 2

    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        for each in queries:
            left, right = each
            left_count, right_count = 0, 0

            while left != right:
                if left > right:
                    left = self.get_parents(left)+1
                    left_count += 1
                else:
                    right = self.get_parents(right)+1
                    right_count += 1

            result.append(left_count+right_count+1)

        return result