class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.values = [-1]*size
            self.size = [1]*size

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, val1, val2, weight):
            root_1 = self.find(val1)
            root_2 = self.find(val2)

            if root_1 == root_2:
                self.values[root_1] &= weight
                return 

            if self.size[root_1] > self.size[root_2]:
                self.parent[root_2] = root_1
                self.values[root_1] &= (weight & self.values[root_2])
                self.size[root_1] += self.size[root_2]
            else:
                self.parent[root_1] = root_2
                self.values[root_2] &= (weight & self.values[root_1])
                self.size[root_2] += self.size[root_1]

        def check_union(self, val1, val2):
            root_1 = self.find(val1)
            root_2 = self.find(val2)

            if root_1 == root_2:
                return True
            return False
            

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        union_find = self.UnionFind(n)

        for edge in edges:
            _ = union_find.union(edge[0], edge[1], edge[2])

        result = []
        for each in query:
            if union_find.check_union(each[0], each[1]):
                result.append(union_find.values[union_find.find(each[0])])
            else:
                result.append(-1)
        
        return result