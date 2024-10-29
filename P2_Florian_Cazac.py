from ortools.linear_solver import pywraplp
import os

def solve_with_or_tools():
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        print("Solver not created. Check OR-Tools installation.")
        return None

    # Create variables
    x = solver.NumVar(0, solver.infinity(), "x")
    y = solver.NumVar(0, solver.infinity(), "y")

    # Create objective function
    os.system("cls")
    print("Objective Function section:")
    objective = solver.Objective()
    objective.SetCoefficient(x, float(input("Enter the coefficient for x in the objective: ")))
    objective.SetCoefficient(y, float(input("Enter the coefficient for y in the objective: ")))
    objective.SetMaximization()

    # Create constraints
    os.system("cls")
    print("\nConstraints section:")
    nb_constraints = int(input("Enter the number of constraints: "))

    for i in range(nb_constraints):
        print(f"\nConstraint {i + 1}:")
        constraint_lb = float(input("Enter the lower bound (>=) (or -inf for no lower bound): "))
        constraint_ub = float(input("Enter the upper bound (<=) (or inf for no upper bound): "))
        
        if constraint_lb == -float("inf"):
            constraint_lb = -solver.infinity()
        if constraint_ub == float("inf"):
            constraint_ub = solver.infinity()
        
        constraint = solver.Constraint(constraint_lb, constraint_ub)
        constraint.SetCoefficient(x, float(input("Enter the coefficient for x in this constraint: ")))
        constraint.SetCoefficient(y, float(input("Enter the coefficient for y in this constraint: ")))

    # Solve the system.
    os.system("cls")
    print(f"\nSolving with {solver.SolverVersion()}...")
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("\nSolution:")
        print(f"Objective value = {solver.Objective().Value():0.1f}")
        print(f"x = {x.solution_value():0.1f}")
        print(f"y = {y.solution_value():0.1f}")
    else:
        print("The problem does not have an optimal solution.")

    print("\nAdvanced usage:")
    print(f"Problem solved in {solver.wall_time():d} milliseconds")
    print(f"Problem solved in {solver.iterations():d} iterations")


if __name__ == "__main__":
    solve_with_or_tools()
