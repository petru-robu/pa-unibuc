if __name__ == '__main__':
    m, n, k = input().split()
    m, n, k = int(m), int(n), int(k)

    mat= []
    for i in range(0, m):
        l = input().split()
        for j in range(len(l)):
            l[j] = int(l[j])
        mat.append(l)

    mat.insert(k, [0]*n)
    print(mat)
        

