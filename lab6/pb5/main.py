if __name__ == '__main__':

    f1 = open('cuvinte1.in', 'r')
    f2 = open('cuvinte2.in', 'r')

    df1, df2 = {}, {}

    for line in f1:
        for word in line.split():
            if word in df1:
                df1[word] += 1
            else:
                df1[word] = 1

    for line in f2:
        for word in line.split():
            if word in df2:
                df2[word] += 1
            else:
                df2[word] = 1

    print(df1)
    print(df2)

    common = []

    for key in df1:
        if key in df2:
            common.append(key)

    print(common)

    
