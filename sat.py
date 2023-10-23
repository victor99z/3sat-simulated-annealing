import random
import utils

class ThreeSAT:
    clauses : list = []
    variables : set[int] = set()
    initial_solution : list[int] = []
    num_clauses = 0

    def __init__(self, filename: str) -> None:
        self.clauses, self.variables = utils.read_file(filename)
        self.initial_solution = self.generate_solution()
        self.num_clauses = len(self.clauses)

    def generate_solution(self) -> list[int]:
        return [random.choice([True, False]) for _ in range(len(self.variables))]

    # def read_from_file(self, filaname: str) -> None:
    #     with open(filaname, 'r', encoding='utf-8') as f:
    #         for line in f:
    #             if line.startswith('%'):
    #                 break
    #             if line.startswith('c'):
    #                 continue
    #             if line.startswith('p'):
    #                 continue
    #             clause = [int(x) for x in line.split()]
    #             clause.pop() # remove the last 0, 0 = AND operator
                
    #             self.clauses.append(clause)
    #             for x in clause:
    #                 self.variables.add(abs(x))

    def evaluate(self, solution : list[int]):
        satisfied = 0
        for clause in self.clauses:

            a = not solution[abs(clause[0]) - 1] if clause[0] < 0 else solution[abs(clause[0]) - 1]
            b = not solution[abs(clause[1]) - 1] if clause[1] < 0 else solution[abs(clause[1]) - 1]
            c = not solution[abs(clause[2]) - 1] if clause[2] < 0 else solution[abs(clause[2]) - 1]

            # a = clause[0] < 0 and not solution[abs(clause[0]) - 1] or clause[0] > 0 and solution[abs(clause[0]) - 1]
            # b = clause[1] < 0 and not solution[abs(clause[1]) - 1] or clause[1] > 0 and solution[abs(clause[1]) - 1]
            # c = clause[2] < 0 and not solution[abs(clause[2]) - 1] or clause[2] > 0 and solution[abs(clause[2]) - 1]

            if a or b or c:
                satisfied += 1

        return satisfied