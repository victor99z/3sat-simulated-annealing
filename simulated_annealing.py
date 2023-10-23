import math
from sat import ThreeSAT
import random
import numpy as np

class Annealing:

    def __init__(self, sat: ThreeSAT, max_iterations, cooling_schedule = 8,temp = 1, temp_min = 0.001, sa_max = 1) -> None:
        self.sat = sat
        self.max_iterations = max_iterations
        self.temp = temp
        self.temp_inicial = temp
        self.temp_min = temp_min
        self.score = self.sat.evaluate(self.sat.initial_solution)
        self.solution = self.sat.initial_solution.copy()
        self.score_list = np.array([])
        self.temp_list = np.array([])
        self.acceptance_probability_list = []
        self.cooling_schedule = cooling_schedule
        self.sa_max = sa_max

    def calc_neighbour(self):
        neighbour = self.solution.copy()
        generateRandomSeed = random.randint(0, len(neighbour)-1)
        neighbour[generateRandomSeed] = not neighbour[generateRandomSeed]
        return neighbour

    def acceptance_probability(self, score, new_score, temp):
            if temp <= 0:
                return 0
            return np.exp((new_score - score) / (temp))

    def calc_temp(self, it):
        match self.cooling_schedule:
            case 0:
                return self.calc_temp_0(it)
            case 1:
                return self.calc_temp_1(it)
            case 2:
                return self.calc_temp_2(it)
            case 8:
                return self.calc_temp_8(it)

    # Cooling schedule 0
    def calc_temp_0(self, it : int):
        return self.temp_inicial - it*(self.temp_inicial-self.temp_min)/self.max_iterations

    def calc_temp_8(self, it : int):
        A = (1/self.max_iterations) * math.log(self.temp_inicial/self.temp_min)
        t_i = self.temp_inicial * math.exp(-A * it) 
        return t_i

    # Cooling Schedule 2
    def calc_temp_2(self, it : int):
        A = ((self.temp_inicial - self.temp_min) * (self.max_iterations + 1)) / self.max_iterations
        B = self.temp_inicial - A
        T = (A / (it + 1)) + B
        return T

    # Cooling Schedule 1
    def calc_temp_1(self, it : int):
        return self.temp_inicial * ((self.temp_min / self.temp_inicial) ** (it / self.max_iterations))

    def run(self):
        iterations = 0
        while self.temp > self.temp_min:
            i = 1
            while i <= self.sa_max:
                new_solution = self.calc_neighbour()
                new_score = self.sat.evaluate(new_solution)
                if new_score > self.score:
                    self.score = new_score
                    self.solution = new_solution
                else:
                    calc_prob = self.acceptance_probability(self.score, new_score, self.temp)
                    print(self.score, new_score, self.temp, calc_prob, sep=";")
                    if random.uniform(0,1) < calc_prob:
                        self.score = new_score
                        self.solution = new_solution
                    self.acceptance_probability_list.append(calc_prob)
                i += 1
            self.temp = self.calc_temp(iterations)
            self.temp_list = np.append(self.temp_list, self.temp)
            self.score_list = np.append(self.score_list, self.score) # Salva uma lista de iterações e num de clausulas não satistifeitas
            iterations += 1