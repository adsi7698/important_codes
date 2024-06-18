class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        frequency = {}

        for i in power:
            if i not in frequency.keys():
                frequency[i] = 1
            else:
                frequency[i] += 1

        power = sorted(list(set(power)))
        opt = [0]*len(power)
        opt[0] = power[0]*frequency[power[0]]

        for i in range(1, len(power)):
            temp = power[i]*frequency[power[i]]
            check_val = power[i]

            for j in range(i-1, -1, -1):
                if check_val - 2 <= power[j]:
                    continue
                temp += opt[j]
                break

            opt[i] = max(opt[i-1], temp)

        return max(opt)

            


