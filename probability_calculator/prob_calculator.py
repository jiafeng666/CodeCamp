import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            # self.__setattr__(key, value)
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        choices = []
        for i in range(num):
            cho = random.choice(self.contents)
            choices.append(cho)
            self.contents.remove(cho)
        return choices


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    fit_num = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_result = hat_copy.draw(num_balls_drawn)
        num = 0
        for key, value in expected_balls.items():
            if draw_result.count(key) < value:
                break
            else:
                num += 1
        if num == len(expected_balls):
            fit_num += 1
    return fit_num / num_experiments


if __name__ == '__main__':
    hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
    probability = experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1},
                             num_balls_drawn=20, num_experiments=100)
    print(probability)

