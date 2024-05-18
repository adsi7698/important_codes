class Solution:
    def minPartitions(self, n: str) -> int:
        highest = 0
        for each in n:
            if int(each) > highest:
                highest = int(each)

        return highest