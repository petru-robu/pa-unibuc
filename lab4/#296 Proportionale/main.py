if __name__ == '__main__':
    n = int(input())
    a = input().split()
    b = input().split()

    for i in range(n):
        a[i] = int(a[i])
        b[i] = int(b[i])

    a.sort()
    b.sort()

    for i in range(1, n):
        if a[0] * b[i] != b[0] * a[i]:
            print('NU')
            exit(0)
    
    print('DA')
