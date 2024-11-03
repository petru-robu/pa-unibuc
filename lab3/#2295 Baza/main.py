
if __name__ == '__main__':
    f = open("baza.in", "r")
    g = open("baza.out", "w")

    s = f.read()
    p = 1
    ans = 0

    for c in s[::-1]:
        val = ord(c) - ord('a')
        ans += p*val
        p *= 26

    print(ans, file=g)