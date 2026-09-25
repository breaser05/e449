import matplotlib.pyplot as plt
import numpy as np


# Gradient Descent LOBF calculator
# Henry Saam ,Laksh Solanki, Bryce Reaser
# the m and b are intialized to two numbers but can be changed for various different values then I caulated the two vectors of the
# two partial deriatives for both m and b then it takes a "step back" in the direction of the negative gradient to find the minimum error and then it does this for # iterations and prints out the final values of m and b and the error
x = np.array([2.9, -1.5, 0.1, -1, 2.1, -4.0, -2.0, 2.2, 0.2, 2, 1.5, -2.5]) #Height 
y = np.array([4.0, -0.9, 0, -1, 3, -5, -3.5, 2.6, 1.0, 3.5, 1, -4.7]) #Weight
m = 2 #intial slope 
b = 2 # intital y intercept
error = 0.0 
perror = 0.0 # previous error


step = 0.01

for iteration in range(100): #doing 100 iteration of gradient descent on all data points the 1000 can be changed
    v1 = np.zeros(len(x))
    v2 = np.zeros(len(x)) 
    for i in range(len(x)):

        v1 = 2 * x[i] * (m*x[i] +b - y[i]) #both vectors calcuate gradient descent
        v2 = 2 * (m*x[i] +b - y[i])
        

    m -= step * np.sum(v1) #going backwards
    b -= step * np.sum(v2)

    
    predictions = m * x + b 
    error = np.mean((predictions - y) ** 2) #MSE error for all error

    if iteration % 100 == 0:
        print(iteration, m, b, error) #print it all out every 100 iterations

line = m * x + b
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x,line, color='red', label='Fitted Line')
plt.show()