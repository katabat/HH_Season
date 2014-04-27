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

def arrangeDates(dates):
    n = (max(dates) - min(dates)).days
    arrdates = []
    for i in range(0,n+1):
        arrdates.append(min(dates) + dt.timedelta(days = i))
    return arrdates

def moving_average(x, n, type='simple'):
    """
    compute an n period moving average.

    type is 'simple' | 'exponential'

    """
    x = np.asarray(x)
    if type=='simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()


    a =  np.convolve(x, weights, mode='full')[:len(x)]
    a[:n] = a[n]
    return a

'''
Find all dates as integer only.
Find all dates not in run dates.
Concatenate run and no_run dates
Sort by date column http://stackoverflow.com/questions/6835531/sorting-a-python-array-recarray-by-column
Convert to datetime object for plotting last!
'''

# Get excel data
f2014 = ('f2014.txt')
d2014 = np.genfromtxt(f2014)

# Convert to datetime dates
date2014 = makeDates(d2014)

#Convert back to nx2 array
run_array = np.array([data2014[:], d2014[:,1]]).T

#Get all dates in range
alldate2014 = arrangeDates(data2014)
# Find none running days
no_run = set(alldate2014).difference(set(date2014))
no_run_array = np.array([(list(no_run)), (np.zeros([len(no_run),1]))]).T
#
#Combine running and non-running data
#2014data = np.concatenate([no_run_array, run_array])

# Weekly average
average = moving_average(run_array[:,1],7)

fig, ax = plt.subplots()

ax.bar(run_array[:,0], run_array[:,1], width = 1, ec = 'none', fc = '#FFCC66')
ax.plot(run_array[:,0], average)
fig.autofmt_xdate()




plt.show()