class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.size = [1]*size
            self.max_size = 1

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)

            if root_x != root_y:
                if self.size[root_y] > self.size[root_x]:
                    self.parent[root_x] = root_y
                    self.size[root_y] += self.size[root_x]
                    self.max_size = max(self.max_size, self.size[root_y])
                    return True
                else:
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]
                    self.max_size = max(self.max_size, self.size[root_x])
                    return True

            return False

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # kruskal

        sorted_edges = []
        for i, edge in enumerate(edges):
            sorted_edges.append(edge+[i])

        sorted_edges.sort(key = lambda x: x[2])

        union_find = self.UnionFind(n)
        minimum_spt = 0
        for i, j, weight, _ in sorted_edges:
            if union_find.union(i, j):
                minimum_spt += weight

        critical_edges, pseudo_critical_edges = [], []
        for i, j, weight, index in sorted_edges:
            temp_union_find = self.UnionFind(n)
            temp_min_weight = 0

            for temp_i, temp_j, temp_weight, temp_index in sorted_edges:
                if temp_index != index and temp_union_find.union(temp_i, temp_j):
                    temp_min_weight += temp_weight

            if temp_union_find.max_size < n or temp_min_weight > minimum_spt:
                critical_edges.append(index)
                continue

            psuedo_union_find = self.UnionFind(n)
            psuedo_min_weight = weight
            psuedo_union_find.union(i, j)
            for psuedo_i, psuedo_j, psuedo_weight, psuedo_index in sorted_edges:
                if psuedo_index != index and psuedo_union_find.union(psuedo_i, psuedo_j):
                    psuedo_min_weight += psuedo_weight

            if psuedo_min_weight == minimum_spt:
                pseudo_critical_edges.append(index)

        return [critical_edges, pseudo_critical_edges]
