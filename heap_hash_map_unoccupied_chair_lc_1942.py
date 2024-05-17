import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        time_list = [[10**5+2] for _ in range(10**5+1)]

        for index in range(len(times)):
            if time_list[times[index][0]][0] == 10**5+2:
                time_list[times[index][0]] = [index+1]
            else:
                time_list[times[index][0]].append(index+1)

            if time_list[times[index][1]][0] == 10**5+2:
                time_list[times[index][1]] = [-(index+1)]
            else:
                time_list[times[index][1]].append(-(index+1))

        used = {}
        unused = [x for x in range(len(times))]
        heapq.heapify(unused)
        count = 0
        for i in range(len(time_list)):
            if count == len(times)*2:
                break

            time_list[i] = sorted(time_list[i])

            for each in time_list[i]:
                if each == 10**5+2:
                    continue

                count += 1
                if each > 0:
                    chair = heapq.heappop(unused)
                    used[each-1] = chair
                    if targetFriend == each-1:
                        return chair
                else:
                    chair = used[-(each+1)]
                    del used[-(each+1)]
                    heapq.heappush(unused, chair)
        return -1