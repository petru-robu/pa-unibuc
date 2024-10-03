if __name__ == "__main__":

    v = input().split()
    for i in range(len(v)):
        v[i] = int(v[i])

    v.sort()
    print(v)