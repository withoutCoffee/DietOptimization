# Solution test for diet problem, with simples inside ortools
import json
from ortools.linear_solver import pywraplp

nutrients = []
data = []
with open("data/nutrients.json","r") as openfile:
    nutrients = json.load(openfile)
with open("data/data.json","r") as openfile:
    data = json.load(openfile)

solver = pywraplp.Solver('Diet Problem Example',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Create the variables
foods = [solver.NumVar(0.0,solver.infinity(), item[0]) for item in data]
print('Number of variables:',solver.NumVariables())

# Define Constraints. One constraint per nutrient
constraints = []
for i, nutrient in enumerate(nutrients):
    # constraint >= nutrient value
    constraints.append(solver.Constraint(nutrient[1], solver.infinity()))
    for j, item in enumerate(data):
        nutrient_col = i + 3
        constraints[i].SetCoefficient(foods[j],item[nutrient_col])

print(f"Number of constraints:{solver.NumConstraints()}")

# Objective function: Minimize sum of (price nomalized) foods
objective = solver.Objective()
for food in foods:
    objective.SetCoefficient(food,1)
objective.SetMinimization()

status = solver.Solve()

# Check the problem has an optimal solution.
if status != solver.OPTIMAL:
    print('The problem does not have an optimal solution!')
    if status == solver.FEASIBLE:
        print('A potentially suboptimal solution was found.')
    else:
        print('The solver could not solve the problem.')
        exit(1)

# Display the amounts (in dollars)  to purchase of each food
nutrients_result = [0] * len(nutrients)

for i, food in enumerate(foods):
    if food.solution_value() > 0.0:
        print('{}: ${}'.format(data[i][0], 365. * food.solution_value()))
        for j, _ in enumerate(nutrients):
            nutrients_result[j] += data[i][j + 3] * food.solution_value()
print('\nOptimal annual price: ${:.4f}'.format(365. * objective.Value()))