import random
import numpy as np

def objective_function(X):
    return sum(x**2 for x in X)

def create_individual(n):
    return [random.uniform(-100, 100) for _ in range(n)]

def create_population(pop_size, n):
    return [create_individual(n) for _ in range(pop_size)]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.uniform(-100, 100)

def select_individual(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            return individual

def genetic_algorithm(n, pop_size, generations, mutation_rate):
    population = create_population(pop_size, n)
    for generation in range(generations):
        fitnesses = [objective_function(ind) for ind in population]
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select_individual(population, fitnesses)
            parent2 = select_individual(population, fitnesses)
            offspring1, offspring2 = crossover(parent1, parent2)
            mutate(offspring1, mutation_rate)
            mutate(offspring2, mutation_rate)
            new_population.extend([offspring1, offspring2])
        population = new_population
        
        # Print statistics
        best_individual = max(population, key=objective_function)
        best_fitness = objective_function(best_individual)
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    best_individual = max(population, key=objective_function)
    return best_individual, objective_function(best_individual)

if __name__ == "__main__":
    n = 10  # Number of dimensions
    pop_size = 10  # Population size
    generations = 10  # Number of generations
    mutation_rate = 0.2  # Mutation rate

    best_individual, best_fitness = genetic_algorithm(n, pop_size, generations, mutation_rate)
    print("Best Individual:", best_individual)
    print("Best Fitness:", best_fitness)
