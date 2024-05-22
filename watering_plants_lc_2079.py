class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        original_capacity = capacity
        result = 0
        for i in range(len(plants)):
            if plants[i] <= capacity:
                result += 1
                capacity -= plants[i]
            else:
                capacity = original_capacity
                result += (2*i + 1)
                capacity -= plants[i]

        return result