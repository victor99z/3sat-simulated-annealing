import sat

class RandomSearch:
    
    def __init__(self, sat: sat.ThreeSAT, max_iterations: int):
        self.sat = sat
        self.max_iterations = max_iterations
        self.score = []

    def run(self) -> list[int]:
        """
            Implement the random search algorithm
        """
        best_solution = self.sat.initial_solution
        best_score = self.sat.evaluate(best_solution)
        for _ in range(self.max_iterations+1):
            solution = self.sat.generate_solution()
            score = self.sat.evaluate(solution)
            if score > best_score:
                best_solution = solution
                best_score = score
            self.score.append(self.sat.num_clauses - score)
        return best_solution