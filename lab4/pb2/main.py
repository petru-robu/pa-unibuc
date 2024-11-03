
if __name__ == '__main__':
    s, n = "test", 3

    ces = [chr((ord(a) + n)) for a in s]
    print("".join(ces))