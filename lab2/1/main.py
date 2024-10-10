
if __name__ == "__main__":
    n = int(input())
    cn = n
    ogl = 0

    while cn:
        ogl = ogl*10 + cn%10
        cn//=10
    
    if n == ogl:
        print("Palindrom")
    else:
        print("Nu e Palindrom")