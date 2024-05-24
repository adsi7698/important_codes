class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        result = [0]*k
        hash_maps = {}

        for each in logs:
            if each[0] not in hash_maps.keys():
                hash_maps[each[0]] = [[each[1]], 1]
            else:
                if each[1] not in hash_maps[each[0]][0]:
                    hash_maps[each[0]][0].append(each[1])
                    hash_maps[each[0]][1] += 1
        
        for value in hash_maps.values():
            result[value[1]-1] += 1

        return result


        