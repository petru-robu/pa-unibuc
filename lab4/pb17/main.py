if __name__ == '__main__':
    l = [1.2, 1.3, -5.4, -3.3, 4.6, 1.2, 7, -8, 1.0]

    i = 0
    while i < len(l):
        if l[i] < 0:
            l.insert(i+1, 0)
            i+=1
        i+=1

    print(l)