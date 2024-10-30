from ortools.linear_solver import pywraplp
import os
import numpy as np
import pandas as pd


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
    max_min = input("Enter 'max' for maximization or 'min' for minimization: ").lower()
    objective = solver.Objective()
    objective.SetCoefficient(x, float(input("Enter the coefficient for x in the objective: ")))
    objective.SetCoefficient(y, float(input("Enter the coefficient for y in the objective: ")))
    
    
    if max_min == "max":
        objective.SetMaximization()
    elif max_min == "min":
        objective.SetMinimization()
    else:
        print("Invalid input. Please enter 'max' or 'min'.")
        return None

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


def print_tableau(tableau, iteration):
    print(f"\nIteration {iteration}")
    print("Tableau:")
    print(tableau)

def simplex_method():
    

    num_vars = 2  # Fixed number of variables
    num_constraints = int(input("Enter the number of constraints: "))

    # Input objective function coefficients
    os.system("cls")
    print("Objective Function section:")
    print("Enter the coefficients of the objective function:")
    objective_func = [float(input(f"Coefficient for x{i+1}: ")) for i in range(num_vars)]
    objective_func.extend([0] * num_constraints)  # Slack variables have zero cost
    objective_func = np.array(objective_func)

    # Input constraint matrix and bound vector
    os.system("cls")
    print("Constraints section:")
    constraint = []
    bound = []
    for i in range(num_constraints):
        print(f"\nEnter coefficients for constraint {i+1}:")
        row = [float(input(f"Coefficient for x{j+1}: ")) for j in range(num_vars)]
        # Add slack variable for the current constraint
        row.extend([1 if i == j else 0 for j in range(num_constraints)])
        constraint.append(row)
        bound.append(float(input("Right-hand side value: ")))
    
    constraint = np.array(constraint)
    bound = np.array(bound)
    
    # Initialize the tableau
    os.system("cls")
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    tableau[:num_constraints, :num_vars + num_constraints] = constraint
    tableau[:num_constraints, -1] = bound
    tableau[-1, :num_vars + num_constraints] = -objective_func
    
    # Start simplex algorithm iterations
    iteration = 0
    while True:
        print_tableau(tableau, iteration)
        # Check if the solution is optimal (no negative entries in the last row)
        if all(tableau[-1, :-1] >= 0):
            print("\nOptimal solution found.")
            break

        # Determine entering variable (most negative in the last row)
        entering = np.argmin(tableau[-1, :-1])

        # Determine leaving variable (smallest positive ratio in column)
        ratios = []
        for i in range(num_constraints):
            if tableau[i, entering] > 0:
                ratios.append(tableau[i, -1] / tableau[i, entering])
            else:
                ratios.append(np.inf)  # Non-positive entries ignored in min ratio test

        leaving = np.argmin(ratios)
        
        if ratios[leaving] == np.inf:
            print("The solution is unbounded.")
            return None
        
        # Pivot
        pivot = tableau[leaving, entering]
        tableau[leaving] /= pivot  # Normalize pivot row

        for i in range(num_constraints + 1):
            if i != leaving:
                tableau[i] -= tableau[i, entering] * tableau[leaving]

        iteration += 1
    
    # Solution
    solution = np.zeros(num_vars)
    for i in range(num_constraints):
        if np.sum(tableau[i, :num_vars]) == 1:
            col = np.argmax(tableau[i, :num_vars])
            if tableau[-1, col] == 0:
                solution[col] = tableau[i, -1]
    
    print("\nOptimal solution:", solution)
    print("Optimal value:", tableau[-1, -1])
    return solution, tableau[-1, -1]


def display_menu():
    os.system("cls")
    print("Choose the method you want to use:")
    print("1. OR-Tools")
    print("2. Simplex Method")
    print("3. Exit")


def menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("cls")
            solve_with_or_tools()
            input("Press Enter to continue...")
        elif choice == "2":
            os.system("cls")
            simplex_method()
            input("Press Enter to continue...")
        elif choice == "3":
            break
        else:
            os.system("cls")
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")
    

    
if __name__ == "__main__":
    menu()