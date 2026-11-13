import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("data(Sheet1).csv", delimiter=",", dtype=str)
# data should be an np array. Write a temporary line of code that
# prints the first row of the array to check that this worked.
print (data)
x= data[1:, 0].astype(np.float32)
y= data[1:,1].astype(np.float32)
print("y = ", y)
print("x = ", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
#exercise 1
x_unit="g"
y_unit="cm"
print_equation(slope, intercept, y_unit, x_unit)
#The equation of the line is y=-0.0044 g/cmx+5.9714cm
fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("weight (g)") #change the units as appropriate
plt.ylabel("height (cm)")  #change the units as appropriate
plt.show()
fig.savefig('squishyplot.png') # Please use this command to save your plots as PNG files
