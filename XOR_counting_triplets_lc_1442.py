class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                temp = arr[i]
                for k in range(i+1, j+1):
                    temp = temp ^ arr[k]

                if temp == 0:
                    count += (j-i)

        return count
