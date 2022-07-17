from ortools.linear_solver import pywraplp
import json

class Diet_Model:
    """Optimizarion class with generic solution for
    Diet Problem, with google Ortools.
    """
    _days = 7  # days of diet
      
    def __init__(self,*args,**kwargs):
        self._nutrients = kwargs.get("nutrients")
        self._data = kwargs.get("data")

    def _get_data(self):
        return self._nutrients, self._data
        
    def _load_constraints(self):
        self._solver = pywraplp.Solver("Diet Price Problem",pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
        self._foods = [self._solver.NumVar(0.0,self._solver.infinity(), item[0]) for item in self._data]
        # Load Constraints
        # Define Constraints. One constraint per nutrient
        self._constraints = []
        for i, nutrient in enumerate(self._nutrients):
            # constraint >= nutrient value
            self._constraints.append(self._solver.Constraint(nutrient[1], self._solver.infinity()))
            for j, item in enumerate(self._data):
                nutrient_col = i + 3
                self._constraints[i].SetCoefficient(self._foods[j],item[nutrient_col])
        
        #print('Number of variables:',self._solver.NumVariables())
        #print(f"Number of constraints:{self._solver.NumConstraints()}")


    def _fit(self):
            # Objective function: Minimize sum of (price nomalized) foods
        self._objective = self._solver.Objective()
        for food in self._foods:
            self._objective.SetCoefficient(food,1)
        self._objective.SetMinimization()


    def _result(self):
        status = self._solver.Solve()
        # Check the problem has an optimal solution.
        if status != self._solver.OPTIMAL:
            #print('The problem does not have an optimal solution!')
            if status == self._solver.FEASIBLE:
                pass#print('A potentially suboptimal solution was found.')
            else:
                #print('The solver could not solve the problem.')
                return 'The solver could not solve the problem.'
        # Display the amounts (in dollars)  to purchase of each food
        nutrients_result = [0] * len(self._nutrients)
        result = {}
        for i, food in enumerate(self._foods):
            if food.solution_value() > 0.0:
                food_name = 0
                price = 2
                total = self._days * food.solution_value()
                
                result[self._data[i][food_name]] = {f"quantity":total/self._data[i][price],"amount":total}
                
                for j, _ in enumerate(self._nutrients):
                    nutrients_result[j] += self._data[i][j + 3] * food.solution_value()
        amount = self._days * self._objective.Value()
        return result, amount

if __name__ == '__main__':
    diet = Diet(nutrients_path = "data/nutrients.json", data_path = "data/data.json")
    print(diet._get_data())
