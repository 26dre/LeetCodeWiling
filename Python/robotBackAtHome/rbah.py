class Solution:
    def judgeCircle(self, moves: str) -> bool:
        judgeCircleHelper(moves)


def judgeCircleHelper(moves: str):
    virtual_x_pos = 0
    virtual_y_pos = 0

    for move in moves:
        match move:
            case 'U':
                virtual_y_pos += 1
            case 'D':
                virtual_y_pos -= 1
            case 'L':
                virtual_x_pos -= 1
            case 'R':
                virtual_x_pos += 1

    return virtual_x_pos == 0 and virtual_y_pos == 0
