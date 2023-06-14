# Demo of using pulp to solve a linear program
# Based on video by Mohammad T. Irfan:
#  - https://www.youtube.com/watch?v=qa4trkLfvwQ

from pulp import LpProblem, LpMaximize, LpVariable, value, PULP_CBC_CMD

lp = LpProblem("Bakery_Problem)", LpMaximize)

# Define variables
x1 = LpVariable(name="Bodoin_log", cat="Integer", lowBound=0)
x2 = LpVariable(name="Choclate_cake", cat="Integer", lowBound=0)

# Objective function
lp += 10 * x1 + 5 * x2

# Constraints
lp += (5 * x1 + x2 <= 90, "oven")
lp += (x1 + 10 * x2 <= 300, "food_processor")
lp += (4 * x1 + 6 * x2 <= 125, "boiler")

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
print(f"Objective: {lp.objective}")
print(f"Constraints:")
[print(f"{k}: {v}") for k, v in lp.constraints.items()]

# Print solution
print(f"Solution:")
for var in lp.variables():
    print(f"{var} = {value(var)}")
print(f"Optimum cost = {value(lp.objective)}")
