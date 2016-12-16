#coding=utf8

from time import time

def dp(V, N, items):
    """
    dynamic programming
    """
    print '======================================'
    print 'dynamic programming algorithm'
    start = time()
    
    # state transfer function
    f = []
    for i in xrange(N + 1):
        f.append([])
        for j in xrange(V + 1):
            f[-1].append(0)

    for i in xrange(1, N + 1):
        weight, value = items[i - 1]
        for v in xrange(V + 1):
            if v >= weight:
                f[i][v] = max(f[i - 1][v], f[i - 1][v - weight] + value)
            else:
                f[i][v] = f[i-1][v]
    print f[N][V]
    print 'Time used: ', time() - start

if __name__ == '__main__':
    from data_handler import load_data
    V, N, items = load_data()
    dp(V, N, items)
