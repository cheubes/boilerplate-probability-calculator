import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items() :
            for i in range(0, value) :
                self.contents.append(key)

    def draw(self, nb):
        result = []
        for i in range(0, nb) :
            if len(self.contents) == 0 :
                break
            result.append(self.contents.pop(random.randrange(len(self.contents))))
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for i in range(0, num_experiments) :
        experiment_hat = copy.deepcopy(hat)
        draw_result = experiment_hat.draw(num_balls_drawn)
        success = True
        for expected_color, expected_num in expected_balls.items() :
            color_num = draw_result.count(expected_color)
            success = success and (color_num >= expected_num)
        if success :
            num_success += 1
    return num_success / num_experiments
