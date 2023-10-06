import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls_to_draw):
        drawn_balls = []
        if num_balls_to_draw >= len(self.contents):
            return self.contents  # Return all balls if drawing more than available
        for _ in range(num_balls_to_draw):
            ball_index = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents.pop(ball_index))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**hat.__dict__)  # Create a copy of the original hat
        balls_drawn = hat_copy.draw(num_balls_drawn)
        # Check if the drawn balls match the expected balls
        """match = True
        for color, quantity in expected_balls.items():
            if balls_drawn.count(color) < quantity:
                match = False
                break
        if match:
            successful_draws += 1"""
        # Check if the drawn balls match the expected balls Note "all" return True if iterable matches the iterable
        match = all(balls_drawn.count(key) >= value for key, value in expected_balls.items())
        if match:           # That is True
            successful_draws += 1

    probability = successful_draws / num_experiments
    return probability

# Example usage:
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
