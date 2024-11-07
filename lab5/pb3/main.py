if __name__ == '__main__':
    m, n = input().split()
    m, n = int(m), int(n)

    mat, ans = [], []
    for i in range(0, m):
        l = input().split()
        for j in range(len(l)):
            l[j] = int(l[j])
        ans.append(max(l))
        mat.append(l)

    print(ans)
        

