from sat import ThreeSAT
from random_search import RandomSearch
from simulated_annealing import Annealing
import matplotlib.pyplot as plt
import numpy as np
from time import time

if __name__ == "__main__":

    files = ["uf20-01.cnf", "uf100-01.cnf", "uf250-01.cnf"]

    sat = ThreeSAT("./cases/" + files[0])

    start_time = time()
    testing_sa = Annealing(sat=sat, max_iterations=250000, temp=1, temp_min=0.000001)
    testing_sa.run()
    figure, axis = plt.subplots(2, 1) 

    axis[0].plot(testing_sa.score_list) 
    axis[0].set_xlabel("Iteração")
    axis[0].set_ylabel("Clausulas satisfeitas") 

    axis[1].plot(testing_sa.temp_list, color='red') 
    axis[1].set_xlabel("Iteração")
    axis[1].set_ylabel("Temperatura")

    plt.savefig('./rs/' + files[0] + '_exec001.png')

    # axis[2].scatter(testing_sa.acceptance_probability_list[:],testing_sa.acceptance_probability_list, color='blue') 
    # axis[2].set_title("Probabilidade de aceitação") 

    # Salvar imagem em png depois 

    # """
    #     Testing Random Search
    # """
    # start_time = time()
    # ra = RandomSearch(sat=sat, max_iterations=250000)
    # print(ra.run())
    # print(ra.score.mean(), ra.score.std())
    # plt.plot(ra.score)
    # plt.title("RS - (Clausulas válidas) " + str(time() - start_time))
    # plt.savefig('./ra/' + files[0] + '_exec001.png')

    # plt.show()
