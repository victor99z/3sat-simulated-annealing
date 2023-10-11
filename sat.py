import random

class ThreeSAT:
    clauses : list[list[int]] = []
    variables : set[int] = set()
    initial_solution : list[int] = []
    num_clauses = 0

    def __init__(self, filename: str) -> None:
        self.read_from_file(filename)
        self.generate_initial_solution()
        self.num_clauses = len(self.clauses)

    def generate_initial_solution(self) -> None:
        self.initial_solution = [random.choice([True, False]) for _ in range(len(self.variables))] 

    def generate_solution(self) -> list[int]:
        return [random.choice([True, False]) for _ in range(len(self.variables))]

    def read_from_file(self, filaname: str) -> None:
        with open(filaname) as f:
            for line in f:
                if line.startswith('%'):
                    break
                if line.startswith('c'):
                    continue
                if line.startswith('p'):
                    _, _, _, n = line.split()
                    n = int(n)
                    continue
                clause = [int(x) for x in line.split()]
                clause.pop()
                self.clauses.append(clause)
                for x in clause:
                    self.variables.add(abs(x))

    def evaluate(self, solution : list[int]):
        satisfied = 0
        for clause in self.clauses:
            a = clause[0] < 0 and not solution[abs(clause[0]) - 1] or clause[0] > 0 and solution[abs(clause[0]) - 1]
            b = clause[1] < 0 and not solution[abs(clause[1]) - 1] or clause[1] > 0 and solution[abs(clause[1]) - 1]
            c = clause[2] < 0 and not solution[abs(clause[2]) - 1] or clause[2] > 0 and solution[abs(clause[2]) - 1]

            if a and b and c:
                satisfied += 1

        return satisfied