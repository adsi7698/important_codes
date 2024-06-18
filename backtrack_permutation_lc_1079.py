import math

class Solution:
    def initialize(self):
        self.count = 0
        self.hash_maps = {}
    
    def rec_backtrack(self, tiles):
        if len(tiles) == 1:
            if tiles not in self.hash_maps:
                self.hash_maps[tiles] = 1
                self.count += 1
            return

        for i in range(len(tiles)):
            self.rec_backtrack(tiles[:i] + tiles[i+1:])
            sorted_temp = ''.join(sorted(tiles))
            if sorted_temp not in self.hash_maps.keys():
                self.hash_maps[sorted_temp] = 1

                temp_hash = {}
                for each in tiles:
                    if each not in temp_hash:
                        temp_hash[each] = 1
                    else:
                        temp_hash[each] += 1

                temp_val = math.factorial(len(sorted_temp))
                for value in temp_hash.values():
                    temp_val //= math.factorial(value)
                self.count += temp_val

        return

        
    def numTilePossibilities(self, tiles: str) -> int:
        self.initialize()
        self.rec_backtrack(tiles)

        return self.count