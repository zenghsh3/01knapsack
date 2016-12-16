#coding=utf8

import random
import math
from time import time

def init_state(V, N, items):
    state = [0] * N

    cur_w = 0
    cur_v = 0
    i = 0
    while cur_w < V:
        i = random.randint(0, N - 1)
        if state[i] == 0:
            state[i] = 1
            cur_w += items[i][0]
            cur_v += items[i][1]
    state[i] = 0
    cur_w -= items[i][0]
    cur_v -= items[i][1]
    return state, cur_w, cur_v

def sa(V, N, items, t0, beta, alpha, max_iters):
    """
    simulated annealing    

    Args:
        t0: initial temperature
        beta: stopping threshold
        alpha: annealing coefficient
    """
   
    cur_state, cur_w, cur_v = init_state(V, N, items)
    best_v = cur_v
    
    # temperature t
    t = t0
    while t > beta:
        for i in xrange(max_iters):
            tmp_w = cur_w
            tmp_v = cur_v
            tmp_state = cur_state[:]
            # generate neighbor
            a = random.randint(0, N - 1)
            b = random.randint(0, N - 1)
            while b == a:
                b = random.randint(0, N - 1)
            if tmp_state[a] == 0 and tmp_state[b] == 1:
                tmp_state[b] = 0
                tmp_w -= items[b][0]
                tmp_v -= items[b][1]
                tmp_state[a] = 1
                tmp_w += items[a][0]
                tmp_v += items[a][1]
            elif tmp_state[a] == 0 and tmp_state[b] == 0:
                tmp_state[a] = 1
                tmp_w += items[a][0]
                tmp_v += items[a][1]
            elif tmp_state[a] == 1 and tmp_state[b] == 1:
                tmp_state[a] = 0
                tmp_w -= items[a][0]
                tmp_v -= items[a][1]
            else:
                tmp_state[a] = 0
                tmp_w -= items[a][0]
                tmp_v -= items[a][1]
                tmp_state[b] = 1
                tmp_w += items[b][0]
                tmp_v += items[b][1]
            delta = tmp_v - cur_v
            if delta > 0 and tmp_w < V:
                if tmp_v > best_v:
                    best_v = tmp_v
                cur_state = tmp_state[:]
                cur_w = tmp_w
                cur_v = tmp_v
            elif tmp_w < V:
                if random.uniform(0,1) < math.exp(delta / t):
                    cur_state = tmp_state[:]
                    cur_w = tmp_w
                    cur_v = tmp_v
        t *= alpha
    return best_v
     
if __name__ == '__main__':
    from data_handler import load_data
    V, N, items = load_data()
    
    start = time()
    print '======================================'
    print 'simulated annealing algorithm'
 
    t0 = 100
    beta = 0.01
    alpha = 0.9
    max_iters = 10 * N
    runs = 30
    average_v = 0
    for i in xrange(runs):
        best_v = sa(V, N, items, t0, beta, alpha, max_iters)
        average_v += best_v
    average_v /= runs
    print average_v
    print 'Time used: ', time() - start
