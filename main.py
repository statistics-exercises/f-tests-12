import matplotlib.pyplot as plt
import numpy as np

def gen_f_variable( T, N ) : 
  # Your code to generate the random variable described in the text goes here


  
# This code generates a 100 random variables using your function above and 
# plots them on a graph
xvals, yvals = np.linspace(0,100,100), np.zeros(100)
for i in range(100) : yvals[i] = gen_f_variable(10,20)

plt.plot( xvals, yvals, 'ko')
plt.savefig("variables.png")
