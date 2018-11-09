from random import randint

class Universe:
    NETS_LEN = 10

    def __init__(self):
        # TODO: Create random nets.
        print('Wasaa')

    @staticmethod
    def cost_of_example(net, training_case):
        return 0

    @staticmethod
    def cost(net, training_cases):
        cost = 0

        for i in range(len(training_cases)):
            cost += cost_of_example()

        return cost

    @staticmethod
    def get_training_cases():
        LEN = 50
        OUTPUT_LENGTH = 10
        cases = []

        for i in range(LEN):
            input_1 = randint(0, 2 ** OUTPUT_LENGTH - 1)
            input_2 = randint(0, 2 ** OUTPUT_LENGTH - 1)
            output = value_1 + value_2

        return cases

    def run_generation(self):
        training_cases = self.get_training_cases()

        f = lambda net: (net, self.cost(net, training_cases))
        costs = [f for net in self.neural_nets]
