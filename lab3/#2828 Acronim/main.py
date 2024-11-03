
if __name__ == '__main__':
    words = input().split()

    ans =''
    for w in words:
        if w[0].isupper():
            ans += w[0]

    print(ans)