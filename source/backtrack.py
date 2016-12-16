#coding=utf8

from time import time

max_v = 0

def backtrack(V, N, items):
    """
    backtrack algorithm
    """
    print '======================================'
    print 'backtrack algorithm'
    start = time()
 
    # sort items by value/item
    for i in xrange(len(items)):
        item = list(items[i])
        item.insert(2, float(items[i][1]) / items[i][0])
        items[i] = tuple(item)
    items = sorted(items, key=lambda x: x[2], reverse = True)
    dfs(0, 0, 0, V, N, items)
    print max_v
    print 'Time used: ', time() - start

def dfs(i, cur_w, cur_v, V, N, items):
    global max_v
    if i >= N:
        if cur_v > max_v:
            max_v = cur_v
    else:
        # choose i item
        if cur_w + items[i][0] < V:
            dfs(i + 1, cur_w + items[i][0], cur_v + items[i][1], V, N, items)

        # do not choose i item
        if up_bound(i + 1, cur_w, cur_v, V, N, items) > max_v:
            dfs(i + 1, cur_w, cur_v, V, N, items)

def up_bound(i, cur_w, cur_v, V, N, items):
    left = V - cur_w
    bound = cur_v
    while i < N and items[i][0] <= left:
        left -= items[i][0]
        bound += items[i][1]
        i += 1
    if i < N:
        bound += (float(items[i][1]) / items[i][0]) * left
    return bound

if __name__ == '__main__':
    from data_handler import load_data
    V, N, items = load_data()
    backtrack(V, N, items)
