import random
import copy


class Hat:
    def __init__(self, **terms):
        self.contents = []
        for key, value in terms.items():
            self.contents.extend([key] * value)

    def draw(self, num_balls_to_draw):
        items_drawn = []
        if num_balls_to_draw >= len(self.contents):
            return self.contents  # Return all balls if drawing more than available
        for i in range(num_balls_to_draw):
            ball_index = random.randint(0, len(self.contents) - 1)  # Select random index
            items_drawn.append(self.contents.pop(ball_index))   # Store random balls
        return items_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)       # Make copy of object hat which contains self.contents
        balls_drawn = hat_copy.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if balls_drawn.count(key) == value:
                successful_draws += 1
            break
    prob = successful_draws / num_experiments
    return prob


fat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
probability = experiment(hat=fat, expected_balls={"red": 2, "orange": 1}, num_balls_drawn=5,
                         num_experiments=2000)
print(f"Probability = {probability:.4f}")
