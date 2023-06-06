import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed = [99, 96, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

arr3 = np.random.normal(5.0, 1.0, 1000)
arr4 = np.random.normal(10.0, 2.0, 1000)

slope, intercept, r, p, std_err = stats.linregress(arr3, arr4)

def someFunc(arr3):
    return slope * arr3 * intercept

simpleModel = list(map(someFunc, arr3))

plt.scatter(arr3, arr4)
plt.plot(arr3, simpleModel)
plt.show()