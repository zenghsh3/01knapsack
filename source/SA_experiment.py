#coding=utf8

from SA import sa

if __name__ == '__main__':
    from data_handler import load_data
    V, N, items = load_data()

    # test t0
    print '===================='
    print 'test t0'
    beta = 0.01
    alpha = 0.9
    max_iters = 10 * N
    for t0 in [5, 20, 50, 70, 100, 200, 500]:
        best_v = sa(V, N, items, t0, beta, alpha, max_iters)
        print t0, best_v

    # test beta
    print '===================='
    print 'test beta'
    t0 = 100
    alpha = 0.9
    max_iters = 10 * N
    for beta in [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0]:
        best_v = sa(V, N, items, t0, beta, alpha, max_iters)
        print beta, best_v

    # test alpha
    print '===================='
    print 'test alpha'
    t0 = 100
    beta = 0.01
    max_iters = 10 * N
    for alpha in [0.1, 0.3, 0.5, 0.7, 0.9]:
        best_v = sa(V, N, items, t0, beta, alpha, max_iters)
        print alpha, best_v
    
    # test max_iters
    print '===================='
    print 'test max_iters'
    t0 = 100
    alpha = 0.9
    beta = 0.01
    for max_iters in [N, 5 * N, 10 * N, 20 * N, 50 * N, 100 * N]:
        best_v = sa(V, N, items, t0, beta, alpha, max_iters)
        print max_iters, best_v
