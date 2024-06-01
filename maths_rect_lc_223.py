class Solution:
    def check_overlap(self, x_axes, y_axes):
        check1, check2 = False, False
        if (x_axes[2] <= x_axes[1] and x_axes[2] >= x_axes[0]) or (x_axes[0] >= x_axes[2] and x_axes[0] <= x_axes[3]):
            check1 = True

        if (y_axes[2] <= y_axes[1] and y_axes[2] >= y_axes[0]) or (y_axes[0] >= y_axes[2] and y_axes[0] <= y_axes[3]):
            check2 = True

        if check1 and check2:
            return True

        return False

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect_1 = (abs(ax2-ax1) * abs(ay2-ay1))
        rect_2 = (abs(bx2-bx1) * abs(by2-by1))

        x_axes = [ax1, ax2, bx1, bx2]
        y_axes = [ay1, ay2, by1, by2]

        if not self.check_overlap(x_axes, y_axes):
            rect_3 = 0
        else:
            x_axes = sorted(x_axes)[1:3]
            y_axes = sorted(y_axes)[1:3]

            rect_3 = (abs(x_axes[1]-x_axes[0]) * abs(y_axes[1]-y_axes[0]))

        return  rect_1 + rect_2 - rect_3