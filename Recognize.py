from numpy import *
import pylab
from Record import *


def func(x):
    return x**2
 
x_list = list(range(len(frames)))
y_list = []

for i in frames:
    sum_chunk = []
    decoded = fromstring(i, 'Int16')
    for j in decoded:
        sum_chunk.append(func(j))
    y_list.append(sum(sum_chunk))
 
 
pylab.plot(x_list, y_list)
pylab.show()
