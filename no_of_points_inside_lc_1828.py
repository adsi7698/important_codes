import math

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for each_c in queries:
            temp = 0
            for each in points:
                if math.sqrt((each_c[0] - each[0])**2 + (each_c[1] - each[1])**2 ) <= each_c[2]:
                    temp += 1
            result.append(temp)

        return result