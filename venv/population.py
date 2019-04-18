import DNA
import random


class Population:
    def __init__(self, size, target, mutation_rate):
        self.size = size
        self.target = target
        self.population = list()
        self.mating_pool = list()
        self.generations = 0
        self.curr_best = ''
        self.target_score = 1
        self.finished = False
        self.mutation_rate = mutation_rate
        self.curr_max_fit = 0

    def generate_population(self):
        """

        Creates new DNA object and initializes a new phrase (genes) and then calculates its fitness
        """
        for i in range(0, self.size):
            pop_mem = DNA.DNA(len(self.target))
            pop_mem.generate_genes()
            pop_mem.calc_fitness(self.target)
            self.population.append(pop_mem)

    def generate_mating_pool(self):
        max_fitness = 0

        for dna in self.population:
            max_fitness = max(max_fitness, dna.fitness)

        for dna in self.population:
            fitness = dna.fitness / max_fitness
            num_times = int(fitness * 100)
            for j in range(0, num_times):
                self.mating_pool.append(dna)

    def create_children(self):
        """
        Make children to refill population
        :return:
        """
        for i in range(0, len(self.population)):
            rand1 = random.randint(0, len(self.population))
            rand2 = random.randint(0, len(self.population))
            parent1 = self.mating_pool[rand1]
            parent2 = self.mating_pool[rand2]
            child = self.population[i].crossover(parent1, parent2)
            child.mutate(0.01)
            child.calc_fitness(self.target)
            self.population[i] = child
        self.generations += 1

    def find_most_fit(self):
        max_fit = 0.0
        best_genes = 0

        for i in range(0, len(self.population)):
            if self.population[i].fitness > max_fit:
                max_fit = self.population[i].fitness
                best_genes = i

        # print(max_fit)

        self.curr_best = self.population[best_genes].genes_as_string()
        self.curr_max_fit = max_fit
        if max_fit == self.target_score:
            self.finished = True

    def is_finished(self):
        return self.finished

    def get_all_phrases(self):
        all_str = ''

        for dna in self.population:
            all_str += dna.genes_as_string() + '\n'

        return all
