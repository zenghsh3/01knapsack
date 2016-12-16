#coding=utf8

import matplotlib.pyplot as plt

with open('iteration.log', 'rb') as f:
    lines = f.readlines()
    lines = [x.strip().split(' ') for x in lines]
    t = [x[0] for x in lines]
    result = [x[1] for x in lines]
    print t
    print result
    plt.scatter(t, result)
    plt.show()
