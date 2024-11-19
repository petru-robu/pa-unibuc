
if __name__ == '__main__':
    n = int(input())
    m = []
    for i in range(n+1):
        m.append((n+1)*[0])

    for i in range(1, n+1):
        m[i][1], m[n][i]  = i, n-i+1
    
    for i in range(n-1, 0, -1):
        for j in range(2, n+1):
            if i >= j:
                print(i,j)
                m[i][j] = m[i+1][j] + m[i][j-1] + m[i+1][j-1]


    for i in range(1, n+1):
        for j in range(1, i+1):
            print(m[i][j], end=' ')
        print()
