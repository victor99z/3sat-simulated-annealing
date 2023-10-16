import math
from sat import ThreeSAT
import random
import numpy as np

class Annealing:

    def __init__(self, sat: ThreeSAT, max_iterations, temp = 1, temp_min = 0.001) -> None:
        self.sat = sat
        self.max_iterations = max_iterations
        self.temp = temp
        self.temp_min = temp_min
        self.score = self.sat.evaluate(self.sat.initial_solution)
        self.score_list = np.array([])
        self.temp_list = np.array([])
        self.acceptance_probability_list = []

    def calc_neighbour(self):
        neighbour = self.sat.initial_solution.copy()
        generateRandomSeed = random.randint(0, len(neighbour)-1)
        neighbour[generateRandomSeed] = not neighbour[generateRandomSeed]
        return neighbour

    def acceptance_probability(self, score, new_score, temp):
            if temp <= 0:
                return 0
            return np.exp((new_score - score) / (temp))

    # Cooling Schedule 4
    def calc_temp(self, it : int):
        A = ((self.temp - self.temp_min) * (self.max_iterations + 1)) / self.max_iterations
        B = self.temp - A
        T = (A / (it + 1)) + B
        return T

    # Cooling Schedule 1
    # def calc_temp(self, it : int):
    #     return self.temp * ((self.temp_min / self.temp) ** (it / self.max_iterations))

    def run(self):
        iterations = 0
        while iterations < self.max_iterations and self.score < self.sat.num_clauses:
            i = 1
            while i <= 1:
                new_solution = self.calc_neighbour()
                new_score = self.sat.evaluate(new_solution)
                if new_score > self.score:
                    self.score = new_score
                    self.sat.initial_solution = new_solution
                else:
                    calc_prob = self.acceptance_probability(self.score, new_score, self.temp)
                    print(self.score, new_score, self.temp, calc_prob, sep=";")
                    if random.uniform(0,1) < calc_prob:
                        self.score = new_score
                        self.sat.initial_solution = new_solution
                    self.acceptance_probability_list.append(calc_prob)
                i += 1
            self.temp =  self.temp * self.calc_temp(iterations)
            self.temp_list = np.append(self.temp_list, self.temp)
            self.score_list = np.append(self.score_list, self.score) # Salva uma lista de iterações e num de clausulas não satistifeitas
            iterations += 1