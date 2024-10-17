
if __name__ == '__main__':
    prop = input()
    s, t = input().split()

    words = prop.split()
    ans = []

    for w in words:
        if w == s:
            ans.append(t)
        else:
            ans.append(w)

    for w in ans:
        print(w, end=' ')
