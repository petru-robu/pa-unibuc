if __name__ == '__main__':
    punct = '.,?!'

    s = input()
    cuv = ''
    words = set()

    punctuatie, litere_mici, litere_mari = 0,0,0

    for i in range(len(s)):
        if s[i] in punct:
            punctuatie += 1
        elif s[i] >= 'a' and s[i] <= 'z':
            litere_mici += 1
        elif s[i] >= 'A' and s[i] <= 'Z':
            litere_mari += 1
            

    print(litere_mari, litere_mici, punctuatie)