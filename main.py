from sat import ThreeSAT
from random_search import RandomSearch
from simulated_annealing import Annealing
import matplotlib.pyplot as plt
import numpy as np
from time import time

if __name__ == "__main__":

    files = ["uf20-01.cnf", "uf100-01.cnf", "uf250-01.cnf"]

    sat = ThreeSAT("./cases/" + files[0])

    testing_sa = Annealing(sat=sat, max_iterations=250000, cooling_schedule=0,temp=1, temp_min=0.01)
    testing_sa.run()
    figure, axis = plt.subplots(2, 1)
    plt.subplots_adjust(hspace=0.5)

    axis[0].plot(testing_sa.score_list) 
    axis[0].axhline(y=sat.num_clauses, color='r', linestyle='dotted')
    axis[0].set_xlabel("Iteração")
    axis[0].set_ylabel("Clausulas satisfeitas") 
    axis[0].set_title("SA")

    axis[1].plot(testing_sa.temp_list, color='red') 
    axis[1].set_xlabel("Iteração")
    axis[1].set_ylabel("Temperatura")

    plt.savefig(f'./sa/ {files[0]} _exec{1}.png')  

    # """
    #     Testing Random Search
    # """
    # start_time = time()
    # rs = RandomSearch(sat=sat, max_iterations=250000)
    # print(rs.run())
    # print(rs.score.mean(), rs.score.std())
    # plt.plot(rs.score)
    # plt.axhline(y=rs.sat.num_clauses, color='r', linestyle='dotted')
    # plt.title("RS - (Clausulas válidas) " + str(time() - start_time))
    # plt.savefig('./rs/' + files[0] + '_exec001.png')

    # fig = plt.figure(figsize=(10, 10))

    # plt.boxplot([testing_sa.score_list, testing_sa.score_list], showfliers=False)

    # plt.show()
