import DNA
import population

target = 'Hello'

pop = population.Population(size=1000, target=target, mutation_rate=0.02)


while not pop.finished:
    pop.generate_population()

    pop.generate_mating_pool()

    pop.create_children()

    pop.find_most_fit()

    print(pop.curr_max_fit)

    print(pop.curr_best)
#



