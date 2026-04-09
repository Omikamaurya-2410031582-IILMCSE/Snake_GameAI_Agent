import random

class Agent:

    def is_safe(self, x, y, width, height, snake):
        if x >= width or x < 0 or y >= height or y < 0:
            return False
        if [x, y] in snake:
            return False
        return True

    def get_action(self, snake_x, snake_y, food_x, food_y, width, height, block, snake):

        directions = {
            "RIGHT": (snake_x + block, snake_y),
            "LEFT": (snake_x - block, snake_y),
            "UP": (snake_x, snake_y - block),
            "DOWN": (snake_x, snake_y + block)
        }

        safe_moves = []

        # Find safe moves
        for move, (nx, ny) in directions.items():
            if self.is_safe(nx, ny, width, height, snake):
                safe_moves.append(move)

        # Move towards food if safe
        if food_x > snake_x and "RIGHT" in safe_moves:
            return "RIGHT"
        if food_x < snake_x and "LEFT" in safe_moves:
            return "LEFT"
        if food_y > snake_y and "DOWN" in safe_moves:
            return "DOWN"
        if food_y < snake_y and "UP" in safe_moves:
            return "UP"

        # Otherwise choose random safe move
        if safe_moves:
            return random.choice(safe_moves)

        return "UP"