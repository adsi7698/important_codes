class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_maps = {}

        for i in range(len(s)):
            if s[i] not in hash_maps.keys():
                hash_maps[s[i]] = [i]
            else:
                if len(hash_maps[s[i]]) == 1:
                    hash_maps[s[i]].append(i)
                else:
                    hash_maps[s[i]][1] = i

        result = []
        i = 0
        while i < len(s):
            j = i
            if len(hash_maps[s[i]]) == 1:
                end = hash_maps[s[i]][0]
            else:
                end = hash_maps[s[i]][1]
            
            while j <= end:
                if len(hash_maps[s[j]]) == 2 and hash_maps[s[j]][1] > end:
                    end = hash_maps[s[j]][1]
                j += 1

            result.append(len(s[i:j]))
            i = j
        
        return result