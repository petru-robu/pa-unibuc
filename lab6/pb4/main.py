def cmp(x):
    return (-len(x), x)


if __name__ == '__main__':
    f = open('text.in', 'r')

    d = {}

    for line in f:
        for word in line.split():
            s = frozenset(word)
            if s in d:
                d[s].append(word)
            else:
                d[s] = list()
                d[s].append(word)
    
    for key in d:
        group = d[key]
        group.sort(key = cmp)
        for w in group:
            print(w, end=' ')
        print()

        