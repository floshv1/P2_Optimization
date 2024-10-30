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

1. **Run the Application**: Open a terminal, navigate to the directory containing the script, and run:

   ```bash
   python your_script_name.py
   ```

2. **Choose a Method**: The program will prompt you to choose between:
   - **1. OR-Tools**: Use Google OR-Tools for solving the linear programming problem.
   - **2. Simplex Method**: Use the manual implementation of the Simplex algorithm.
   - **3. Exit**: Exit the application.

3. **Input Data**:
   - For both methods, you will be asked to enter:
     - Whether you want to maximize or minimize the objective function.
     - The coefficients of the objective function.
     - The number of constraints and their coefficients.
     - The bounds for each constraint.

4. **View Results**: After processing, the optimal solution (if found) will be displayed along with the value of the objective function.

## Example

### Objective Function:
Maximize: \( z = 22x_1 + 28x_2 \)

### Subject to:
- \( 8x_1 + 10x_2 \leq 3400 \)
- \( 2x_1 + 3x_2 \leq 960 \)
- \( x_1 \geq 0 \)
- \( x_2 \geq 0 \)

### Expected Output:
The output will display the optimal values for \( x_1 \) and \( x_2 \), along with the optimal objective value.

## Code Structure

- `solve_with_or_tools()`: Implements the linear programming solver using Google OR-Tools.
- `simplex_method()`: Implements the Simplex algorithm for solving linear programming problems manually.
- `print_tableau()`: Displays the tableau for each iteration of the Simplex method.
- `display_menu()`: Shows the menu options for the user.
- `menu()`: Manages user input and calls the appropriate functions based on user choice.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.
