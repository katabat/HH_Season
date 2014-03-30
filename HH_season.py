'''
Plot season summary from running data
'''

import matplotlib.pyplot as plt
import numpy as np
import datetime as dt



def makeDates(array):
    n = len(array)
    dates = []
    for i in (xrange(n)):
        dates.append(dt.datetime(1899,12,30) + dt.timedelta(days=int(array[i,0])))
    return dates

def arrangeDates(array,dates):



f2014 = ('f2014.txt')
d2014 = np.genfromtxt(f2014)

date2014 = makeDates(d2014)

plt.bar(date2014,d2014[:,1])
plt.show()