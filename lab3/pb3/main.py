

if __name__ == '__main__':
    s = 'ababababcacababc'
    t = 'abc'

    pos = s.find(t)

    if pos == -1:
        print("Nu")
    else:
        while pos!=-1:
            print(pos)
            pos = s.find(t, pos+len(t))
    