# Demo of using pulp to solve a linear program
# Based on video by Mohammad T. Irfan:
#  - https://www.youtube.com/watch?v=qa4trkLfvwQ

from pulp import LpProblem, LpMaximize, LpVariable, value, lpSum, \
    PULP_CBC_CMD

lp = LpProblem("Bakery_Problem)", LpMaximize)

# Define variables
var_keys = [1, 2]
x = LpVariable.dicts("Bakery_item", var_keys, cat="Integer", lowBound=0)

# Objective function
lp += 10 * x[1] + 5 * x[2]

# Constraints
# lp += (5 * x[1] + x[2] <= 90, "oven")
# lp += (x[1] + 10 * x[2] <= 300, "food_processor")
# lp += (4 * x[1] + 6 * x[2] <= 125, "boiler")

# Generate constraints automatically
const_coeffs = {
    "oven": [[5, 1], 90],
    "food_processor": [[1, 10], 300],
    "boiler": [[4, 6], 125]
}
for name, coeffs in const_coeffs.items():
    coeff_dict = dict(zip(var_keys, coeffs[0]))
    lp += ( lpSum([coeff_dict[k]*x[k] for k in var_keys]) <= coeffs[1], name)

# Solve the LP
#status = lp.solve(PULP_CBC_CMD(msg=False))  # raises error
status = lp.solve()
print("Status:", status)
# 1 : optimal
# 2 : not solved
# 3 : infeasible
# 4 : unbounded
# 5 : undef

# Print details of problem
print(f"Variables:")
[print(f"{k}: {v}") for k, v in x.items()]
print(f"Objective: {lp.objective}")
print(f"Constraints:")
[print(f"{k}: {v}") for k, v in lp.constraints.items()]

# Print solution
print(f"Solution:")
for var in lp.variables():
    print(f"{var} = {value(var)}")
print(f"Optimum cost = {value(lp.objective)}")
