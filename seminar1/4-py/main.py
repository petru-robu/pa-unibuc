#Complexitate O(logN)

if __name__ == '__main__':

    n = int(input())

    p = 1
    while p < n:
        p = (p<<1)

    print(p)