if __name__ == '__main__':
    n = int(input())
    v = input().split()
    for i in range(len(v)):
        v[i] = int(v[i])

    i, j = 0, n-1
    op = 0

    while i < j:
        if v[i] != v[j]:
            if v[i] > v[j]:
                v[j-1] += v[j]
                j -= 1
            else:
                v[i+1] += v[i]
                i += 1
            op += 1
        else:
            i+=1
            j-=1
        #print(v)

    print(op)
        