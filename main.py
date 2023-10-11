from sat import ThreeSAT
from random_search import RandomSearch
from simulated_annealing import Annealing
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    files = ["uf20-01.cnf", "uf100-01.cnf", "uf250-01.cnf"]

    sat = ThreeSAT("./cases/" + files[0])

    ## Random search 
    # testing_rs = RandomSearch(sat=sat, max_iterations=10000)
    testing_sa = Annealing(sat=sat, max_iterations=100000)

    figure, axis = plt.subplots(2, 1) 


    # print(testing_rs.run())
    print(testing_sa.run())
    print(testing_sa.score_list)


    axis[0].plot(testing_sa.score_list) 
    axis[0].set_title("Score") 

    axis[1].plot(testing_sa.temp_list) 
    axis[1].set_title("Temperature")  

    # plt.ylabel("Clausulas não validas")
    # plt.xlabel("Iteração")
    # plt.plot(testing_sa.scoreList)
    # plt.xlim(plt.xlim()[::-1])             # Reverses x axis
    plt.show()
