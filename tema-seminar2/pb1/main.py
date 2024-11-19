if __name__ == '__main__':
    w = input()
    words = input().split()
    ans = set()

    for x in words:
        if len(x) == len(w):
            ans.add(x)

    print(ans)