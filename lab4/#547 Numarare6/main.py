if __name__ == '__main__':
    n = int(input())
    v = input().split()

    for i in range(len(v)):
        v[i] = int(v[i])

    maxim = max(v)
    minim = min(v)

    #cnt = 0
    #for x in v:
    #    if x == maxim - minim:
    #       cnt += 1
    print(v.count(maxim-minim))