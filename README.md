# Linear Programming Solver

This Python application provides a user-friendly interface to solve linear programming problems using two different methods: Google OR-Tools and the Simplex method. Users can input their objective functions and constraints through a command-line interface.

## Features

- Solve linear programming problems using:
  - **OR-Tools**: A high-performance solver provided by Google.
  - **Simplex Method**: A manual implementation of the Simplex algorithm.
- Interactive input for defining objective functions and constraints.
- Display of iterations and the tableau during the Simplex method process.

## Prerequisites

To run this code, ensure you have the following installed:

- Python 3.6 or higher
- `numpy` library
- `pandas` library
- `ortools` library (Google OR-Tools)

You can install the required libraries using pip:

```bash
pip install numpy pandas ortools
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

3. **Choose a Method**: The program will prompt you to choose between:
   - **1. OR-Tools**: Use Google OR-Tools for solving the linear programming problem.
   - **2. Simplex Method**: Use the manual implementation of the Simplex algorithm.
   - **3. Exit**: Exit the application.

4. **Input Data**:
   - For both methods, you will be asked to enter:
     - Whether you want to maximize or minimize the objective function.
     - The coefficients of the objective function.
     - The number of constraints and their coefficients.
     - The bounds for each constraint.

5. **View Results**: After processing, the optimal solution (if found) will be displayed along with the value of the objective function.

## Example Problem

You can test the solver with the following example:

### Problem Statement

Maximize:  
**z = 22 * x_A + 28 * x_B**

Subject to:  
1. **8 * x_A + 10 * x_B <= 3400**  
2. **2 * x_A + 3 * x_B <= 960**  
3. **x_A >= 0**  
4. **x_B >= 0**

### Inputs:
1. Coefficient for **x_A**: 22
2. Coefficient for **x_B**: 28
3. Constraints:
   - **Constraint 1**: 
     - Coefficients for **x_A**: 8, 
     - Coefficients for **x_B**: 10, 
     - Right-hand side: 3400
   - **Constraint 2**: 
     - Coefficients for **x_A**: 2, 
     - Coefficients for **x_B**: 3, 
     - Right-hand side: 960

### Expected Output
The program will display:
- The optimal values for \( x_A \) and \( x_B \).
- The optimal objective value.

## Code Structure

- `solve_with_or_tools()`: Implements the linear programming solver using Google OR-Tools.
- `simplex_method()`: Implements the Simplex algorithm for solving linear programming problems manually.
- `print_tableau()`: Displays the tableau for each iteration of the Simplex method.
- `display_menu()`: Shows the menu options for the user.
- `menu()`: Manages user input and calls the appropriate functions based on user choice.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.