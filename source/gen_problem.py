#coding=utf8

import random

if __name__ == '__main__':
    random.seed(1024)

    # size of bag, V
    N = 500
    
    items = []
    item_weight_sum = 0
    for i in xrange(N):
        weight = random.randint(1, 100)
        value = random.randint(1, 100)
        item_weight_sum += weight
        items.append((weight, value))
    
    # weight of bag is 1/2 items weights
    V = item_weight_sum / 2

    # output problem to txt
    with open('problem.txt', 'wb') as f:
        f.write(str(V) + ' ' + str(len(items)) + '\n')
        for item in items:
            f.write(str(item[0]) + ' ' + str(item[1]) + '\n')
