import sympy as sp
from sympy.plotting import plot

sp.var('x, a, b, c')
y = a*x**2 + 2*b*x + c 

solution1 = sp.solve(y,x); display(solution1)
a = 2; b = 3; c = 1
y = a * x**2 + b*x + c
solution2 = sp.solve(a*x**2 + 2*b*x + c, x); display(solution2)
print("***********************************")
sp.var('x,y')

eq3 = sp.Eq(2*x + 1*y, 3)
eq4 = sp.Eq(1*x + 3*y, 4)

sp.solve([eq3, eq4], [x,y])