
if __name__ == "__main__":
    s = input()
    words = s.split()

    maxlen = -1
    for w in words:
        maxlen = max(maxlen, len(w))
    
    ans = ''

    i = 0
    while i < len(s):
        w = ''
        ok = False
        while i < len(s) and s[i] != ' ':
            if s[i].isalpha():
                ok = True

            w+=s[i]
            i+=1

        if w != '':
            ##print(w)
            if ok and len(w) == maxlen:
                ans += w[::-1]
            else:
                ans += w
        if i < len(s):
            ans += s[i]
        i += 1

    print(ans)