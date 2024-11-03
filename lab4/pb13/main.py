
if __name__ == '__main__':
    l = [1, 2, 3, 0, 4, 5, 6, 7, 0, 1, 2, 3]

    i1 = l.index(0)
    i2 = l.index(0, i1+1)

    l = l[:i1] + l[i2+1:]
    print(l)
    #print(l[i1+1:i2])