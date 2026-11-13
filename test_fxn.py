from fitting_functions import *
m=2
x=3
b=4
line=linear(m,x,b)
print(line)
x_unit="meters"
y_unit="kg"
unit=slope_units(x_unit, y_unit)
print(unit)
print_equation(4, 1, "kg", "meters")
