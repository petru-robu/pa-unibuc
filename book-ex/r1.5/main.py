
def squares1(n):
    s = 0
    for i in range(n+1):
        s += i*i
    return s

def squares2(n):
    s = sum(x*x for x in range(n+1))
    return s

def squares3(n):
    return int(n*(n+1)*(2*n+1)/6)

def squares4(n):
    return sum(x*x for x in range(n+1) if x%2 == 1)

if __name__ == "__main__":

    n = 8
    s1 = squares1(n)
    s2 = squares2(n)
    s3 = squares3(n)
    s4 = squares4(n)

    print(s1, s2, s3, s4)