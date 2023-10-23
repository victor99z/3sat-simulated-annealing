import numpy as np
import seaborn as sns
import time
from sat import ThreeSAT
from random_search import RandomSearch
from simulated_annealing import Annealing
import matplotlib.pyplot as plt
import utils
import pandas as pd

INITIAL_TEMP = 1
TARGET_TEMP = 0.01
MAX_ITERATIONS = 250000
NUM_EXECUTION = 1

files = ["uf20-01.cnf", "uf100-01.cnf", "uf250-01.cnf"]

sats = []

logger_random = open("./result/rs.csv", "a", encoding='utf-8')
logger_sa = open("./result/sa.csv", "a", encoding='utf-8')


for file in files:
    sats.append(ThreeSAT("./cases/" + file))

# for i, sat in enumerate(sats.copy()):
    # """
    #     Testing Random Search
    # """
    
def plot_graph(score_list, temp_list, num_clauses, file, it):
    figure, axis = plt.subplots(2, 1)
    plt.subplots_adjust(hspace=0.5)

    axis[0].plot(score_list) 
    axis[0].axhline(y=num_clauses, color='r', linestyle='dotted')
    axis[0].set_xlabel("Iteração")
    axis[0].set_ylabel("Clausulas satisfeitas") 
    axis[0].set_title("SA")

    axis[1].plot(temp_list, color='red') 
    axis[1].set_xlabel("Iteração")
    axis[1].set_ylabel("Temperatura")
    plt.savefig(f'./sa/ {file} _{it:003}.png')
    plt.close() 

def box_plot(score_list, file, it):
    fig = plt.figure(figsize=(10, 10))
    plt.boxplot(score_list,labels=['Random Search', 'Simulated Annealing'])
    plt.savefig(f'./result_boxplot/{file}_{it:003}.png')
    plt.close() 

# for i,file in enumerate(files):
#     result_sa = np.array([])
#     for it in range(1, NUM_EXECUTION + 1):
#         start_time = time.time()
#         sa = Annealing(sat=sats[i], max_iterations=250000, cooling_schedule=8,temp=1, temp_min=0.01)
#         print(sa.run())
#         result_sa = np.append(result_sa, sa.score_list)
#         plot_graph(sa.score_list, sa.temp_list, sa.sat.num_clauses, file, it)
#         logger_sa.write(f'{file}_{it:003}, {sa.score_list.mean()}, {sa.score_list.std()}\n')    
#     logger_sa.write(f'{file}, {result_sa.mean()}, {result_sa.std()}\n')

"""
    BOXPLOT GENERATE
"""

result_sa = np.array([])
result_rs = np.array([])
for i,file in enumerate(files):
    for it in range(1, NUM_EXECUTION + 1):
        sa = Annealing(sat=sats[i], max_iterations=1000, cooling_schedule=8,temp=1, temp_min=0.01)
        rs = RandomSearch(sat=sats[i], max_iterations=1000)
        print(sa.run())
        print(rs.run())
        result_sa = np.append(result_sa, sa.score_list)
        result_rs = np.append(result_rs, rs.score)
        # plot_graph(sa.score_list, sa.temp_list, sa.sat.num_clauses, file, it)
        # logger_sa.write(f'{file}_{it:003}, {sa.score_list.mean()}, {sa.score_list.std()}\n')    
    # logger_sa.write(f'{file}, {result_sa.mean()}, {result_sa.std()}\n')
        # box_plot([rs.score, sa.score_list], file, it)
    print("========== ", len(result_sa), len(result_rs))
    break

plt.boxplot([result_rs, result_sa], labels=['Random Search', 'Simulated Annealing'], showfliers=False)
plt.savefig(f'./result_boxplot/{files[0]}_{it:003}_2500it.png')
plt.close() 
    


# score_rs = pd.DataFrame(result_rs, columns=['Random Search'])
# score_sa = pd.DataFrame(result_sa, columns=['Simulated Annealing'])
# score_data = pd.concat([score_rs, score_sa])
# sns.set()
# sns.boxplot(score_data)



# for it in range(1, NUM_EXECUTION + 1):
#     start_time = time.time()
#     testing_sa = Annealing(sat=sats[0], max_iterations=MAX_ITERATIONS, cooling_schedule=8,temp=INITIAL_TEMP, temp_min=TARGET_TEMP)
#     print(testing_sa.run())
#     result[1].extend(testing_sa.score_list)
#     logger_sa.write(f'{files[0]}, {rs.score.mean()}, {rs.score.std()}, {str(time.time() - start_time)}\n')
#     # plt.plot(rs.score)

# fig = plt.figure(figsize =(10, 7))

# plt.boxplot(result[0],showfliers=False, labels=['Random Search'])
# plt.savefig(f'./result/ {files[0]} _boxplot.png')
# plt.show()

    # plt.axhline(y=sat.num_clauses, color='r', linestyle='dotted')
    # plt.title("RS - (Clausulas válidas) ")
    # plt.savefig(f'./rs/ {files[i]} _exec{it:003}.png')
    # plt.savefig(f'./rs/{files[i]}.png')
    # plt.show()
