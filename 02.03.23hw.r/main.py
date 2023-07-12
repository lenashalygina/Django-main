#6
def can_afford(s, p, m):
    total_cost = s + p
    if total_cost <= m:
        return "Да"
    else:
        return "Нет"

subscription_cost = 500
pizza_cost = 300
salary = 1000

result = can_afford(subscription_cost, pizza_cost, salary)
print(result)


#7
class Chessboard:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]

    def is_valid_cell(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def is_queen_move_valid(self, start_x, start_y, end_x, end_y):
        if not self.is_valid_cell(start_x, start_y) or not self.is_valid_cell(end_x, end_y):
            raise ValueError("Invalid cell coordinates")

        if start_x == end_x or start_y == end_y or abs(start_x - end_x) == abs(start_y - end_y):
            return True
        else:
            return False

    def is_knight_move_valid(self, start_x, start_y, end_x, end_y):
        if not self.is_valid_cell(start_x, start_y) or not self.is_valid_cell(end_x, end_y):
            raise ValueError("Invalid cell coordinates")

        x_diff = abs(start_x - end_x)
        y_diff = abs(start_y - end_y)
        return (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)

