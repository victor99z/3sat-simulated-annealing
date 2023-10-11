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
        self.score_list = []
        self.temp_list = [] # Retonar qtd de clausulas satisfeitas


    # Calculate neighbour using initial solution and flip a random boolean
    def calc_neighbour(self):
        neighbour = self.sat.initial_solution.copy()
        generateRandomSeed = random.randint(0, len(neighbour)-1)
        neighbour[generateRandomSeed] = not neighbour[generateRandomSeed]
        return neighbour

    def prob_aceitacao(self, score, new_score, temp):
            return np.exp((new_score - score) / (temp))

    # Cooling Schedule 4
    def calc_temp(self, it : int):
        A = ((self.temp - self.temp_min) * (self.max_iterations + 1)) / self.max_iterations
        B = self.temp - A
        T = (A / (it + 1)) + B
        return T

    def run(self):
        iterations = 0
        while self.temp > self.temp_min:
            new_solution = self.calc_neighbour()
            new_score = self.sat.evaluate(new_solution)
            if new_score > self.score:
                self.score = new_score
                self.sat.initial_solution = new_solution
            else:
                calc_prob = self.prob_aceitacao(self.score, new_score, self.temp)
                print(calc_prob)
                if calc_prob < random.randint(0,1):
                    self.score = new_score
            self.temp =  self.temp * self.calc_temp(iterations)
            iterations += 1
            self.temp_list.append(self.temp)
            self.score_list.append(self.sat.num_clauses - self.score) # Salva uma lista de iterações e num de clausulas não satistifeitas