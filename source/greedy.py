#coding=utf8

from time import time

def greedy1(V, N, items):
    """
    choose high value item firstly
    """
    print '======================================'
    print 'greedy algorithm 1'
    print 'choose high value item firstly'
    start = time()
    items = sorted(items, key=lambda x: x[1], reverse=True)
    sum_value = 0
    sum_weight = 0
    for i in xrange(len(items)):
        w, v = items[i]
        if sum_weight + w < V:
            sum_weight += w
            sum_value += v
    print sum_value
    print 'Time used: ', time() - start
    print 

def greedy2(V, N, items):
    """
    choose light weight item firstly
    """
    print '======================================'
    print 'greedy algorithm 2'
    print 'choose light weight item firstly'
    start = time()
    items = sorted(items, key=lambda x: x[0])
    sum_value = 0
    sum_weight = 0
    for i in xrange(len(items)):
        w, v = items[i]
        if sum_weight + w < V:
            sum_weight += w
            sum_value += v
    print sum_value
    print 'Time used: ', time() - start
    print 

def greedy3(V, N, items):
    """
    choose high value/weight item firstly
    """
    print '======================================'
    print 'greedy algorithm 3'
    print 'choose high value/weight item firstly'
    start = time()
    for i in xrange(len(items)):
        item = list(items[i])
        item.insert(2, float(items[i][1]) / items[i][0])
        items[i] = tuple(item)
    items = sorted(items, key=lambda x: x[2], reverse = True)
    sum_value = 0
    sum_weight = 0
    for i in xrange(len(items)):
        w, v, rate = items[i]
        if sum_weight + w < V:
            sum_weight += w
            sum_value += v
    print sum_value
    print 'Time used: ', time() - start
    print 


if __name__ == '__main__':
    from data_handler import load_data
    V, N, items = load_data()
    greedy1(V, N, items)
    greedy2(V, N, items)
    greedy3(V, N, items)
