
if __name__ == '__main__':

    n = int(input())
    v = input().split()

    ap = [0] * 102
    for i in range(len(v)):
        v[i] = int(v[i])
    
    for x in v:
        ap[x] += 1

    res = 0
    for i in range(102):
        if ap[i]:
            res += ap[i]//2

    print(res)