if __name__ == '__main__':
    l = [1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 1, 2, 3] 
    k = 3

    i = 0
    ans = []
    smin = sum(l[:k])

    while i + k - 1 < len(l):
        seq = l[i:i+k]
        s = sum(seq)
        print(seq, s)
        if s < smin:
            smin = s
            ans = seq
        i += 1

    print(ans)