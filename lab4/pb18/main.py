if __name__ == '__main__':
    n = 1001
    ciur = [0] * (n+1)

    i = 2
    while i < n:
        if ciur[i] == 0:
            p = 2
            while i*p < n:
                ciur[i*p] = 1
                p+=1
        i += 1

    i = 2
    ans = []
    while i < len(ciur):
        if not ciur[i]:
            ans.append(i)
        i += 1

    print(ans)

        