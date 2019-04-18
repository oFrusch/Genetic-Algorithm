import random
import string


class DNA:
    def __init__(self, length):
        self.length = length
        self.genes = list()
        self.fitness = 0

    def generate_genes(self):
        for i in range(0, self.length):
            rand = int(random.random() * 52)
            self.genes.append(string.ascii_letters[rand])

    def calc_fitness(self, target):
        cur_fit = 0
        for i in range(0, self.length):
            if self.genes[i] == target[i]:
                cur_fit += 1
        self.fitness = cur_fit / len(target)

    def crossover(self, par1, par2):
        """
        Takes in 2 parent strings and returns a child string that is the combination of them both

        :param par1: first parent
        :param par2: second parent
        :return: first half of first parent concatenated with second half of second parent
        """
        child = DNA(self.length)
        midpoint = int(random.random() * self.length)
        first_half = par1.genes[0:midpoint]
        second_half = par2.genes[midpoint:]
        child.genes = first_half + second_half
        return child

    def mutate(self, rate):
        for i in range(0, len(self.genes)):
            rand = random.random()
            # print(rand)
            if rand < rate:
                rand = int(random.random() * 52)
                self.genes[i] = string.ascii_letters[rand]

    def genes_as_string(self):
        return ''.join(self.genes)
