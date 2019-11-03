import matplotlib.pyplot as plt
import random

x = []
y = []
x.append(0)
y.append(0)

iterations = int(input())

for i in range(0,iterations):
    r = random.random()
    if(r < 0.01):
        NewX = 0
        NewY =  0.16 * y[i]
    elif(r < 0.86):
        NewX =  0.85 * x[i] + 0.04 * y[i]
        NewY = -0.04 * x[i] + 0.85 * y[i] + 1.6
    elif(r < 0.93):
        NewX =  00.2 * x[i] - 0.26 * y[i]
        NewY =  0.23 * x[i] + 0.22 * y[i] + 1.6
    else:
        NewX = -0.15 * x[i] + 0.28 * y[i]
        NewY =  0.26 * x[i] + 0.24 * y[i] + 0.44
    x.append(NewX)
    y.append(NewY)


plt.scatter(x, y, s = 0.2, color ='green') """change the colour if you'd like"""
plt.show() 