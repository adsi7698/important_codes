class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opt = [([], 0, 0)]
        result = set()

        while opt:
            state, left, right = opt.pop()
            if len(state) == 2*n and "".join(state) not in result:
                result.add("".join(state))

            if left < n:
                state.append('(')
                opt.append((state.copy(), left+1, right))
                state.pop()
            
            if right < left:
                state.append(')')
                opt.append((state.copy(), left, right+1))
            

        return list(result)

        