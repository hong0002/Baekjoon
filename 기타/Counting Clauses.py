def is_satisfactory(m, n, clauses):
    # Check if the number of clauses is less than 8
    if m < 8:
        return "unsatisfactory"

    # Create a list to store the assignments of variables
    variables = [None] * n

    # Define a function to check if a clause is satisfied
    def is_clause_satisfied(clause):
        for literal in clause:
            variable = abs(literal)
            value = (literal > 0)  # True if positive, False if negative
            if variables[variable - 1] is not None and variables[variable - 1] != value:
                return False
        return True

    # Check if there exists an assignment for each clause
    for clause in clauses:
        if not is_clause_satisfied(clause):
            return "unsatisfactory"

    # If all clauses are satisfied, return "satisfactory"
    return "satisfactory"

# Input
m, n = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(m)]

# Output
result = is_satisfactory(m, n, clauses)
print(result)
