
if __name__ == '__main__':
    s = "abcde"
    print([s[i:i+len(s)] + s[:i] for i in range(0, len(s))])