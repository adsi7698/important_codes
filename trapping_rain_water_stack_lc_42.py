class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                wall_1_index = stack.pop()

                if len(stack) == 0:
                    break

                cur_height = min(height[stack[-1]], height[i]) - height[wall_1_index]
                distance = i - stack[-1] - 1
                water += (cur_height*distance)

            stack.append(i)

        return water

            