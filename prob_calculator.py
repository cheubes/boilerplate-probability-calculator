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
            result.append(self.contents.pop(random.randrange(len(self.contents))))
        return result


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
