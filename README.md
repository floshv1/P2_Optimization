# Linear Programming Solver

## Description

This project provides a linear programming (LP) solver using two methods:
1. **Google OR-Tools**: A powerful library for combinatorial optimization.
2. **Simplex Method**: A step-by-step implementation of the simplex algorithm with tableau visualization.

The solver can handle arbitrary LP problems with two variables, and it includes a graphical representation of the feasible region, constraints, and the optimal solution.

## Features
- Solves LP problems using Google OR-Tools.
- Step-by-step execution of the simplex method with tableau outputs.
- Graphical representation of the feasible region and the optimal solution.

## Requirements

Make sure you have the following installed:
- Python 3.x
- Google OR-Tools
- NumPy
- Matplotlib

You can install the required libraries using pip:

```bash
pip install ortools numpy matplotlib
```

## Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Run the script:

   ```bash
   python linear_programming_solver.py
   ```

3. Follow the prompts to enter your LP problem:
   - Choose between the OR-Tools method or the Simplex method.
   - Enter the coefficients of the objective function.
   - Enter the constraints for the problem.

4. The program will display the optimal solution along with a graph of the feasible region and the optimal point.

## Example Problem

You can test the solver with the following example:

### Problem Statement

Maximize: 
\[ z = 22x_A + 28x_B \]

Subject to:
\[ 8x_A + 10x_B \leq 3400 \]  
\[ 2x_A + 3x_B \leq 960 \]  
\[ x_A \geq 0 \]  
\[ x_B \geq 0 \]

### Inputs:
1. Coefficient for \( x_A \): 22
2. Coefficient for \( x_B \): 28
3. Constraints:
   - Constraint 1: Coefficients for \( x_A \): 8, Coefficients for \( x_B \): 10, Right-hand side: 3400
   - Constraint 2: Coefficients for \( x_A \): 2, Coefficients for \( x_B \): 3, Right-hand side: 960

### Expected Output
The program will display:
- The optimal values for \( x_A \) and \( x_B \).
- The optimal objective value.

## Example Problems

You can test the solver with different exercises from your linear programming course. Make sure to provide the coefficients and constraints based on the problems presented.