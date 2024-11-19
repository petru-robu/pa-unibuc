if __name__ == '__main__':
    punct = '.,?!'

    s = input()
    cuv = ''
    words = set()

    for i in range(len(s)):
        if s[i] in punct or s[i] == ' ':
            if cuv:
                words.add(cuv)
            cuv = ''
        else:
            cuv += s[i]

    print(words)
    print(len(words))