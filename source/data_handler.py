#coding=utf8

def load_data():
    with open('problem.txt', 'rb') as f:
        lines = [x.strip() for x in f.readlines()]
        V, N = lines[0].split(' ')
        V = int(V)
        N = int(N)
        items = []
        for i in xrange(1, len(lines)):
            w, v = lines[i].split(' ')
            items.append((int(w), int(v)))
        return V, N, items

if __name__ == '__main__':
    V, N, items = load_data()
    print V, N
    print items
