
def cmmdc(a, b):
    while b:
        r = a%b
        a = b
        b = r
    return a
    

if __name__ == "__main__":
    l1, l2 = input().split()
    l1 = int(l1)
    l2 = int(l2)

    print(l1 // cmmdc(l1, l2) * (l2//cmmdc(l1, l2))) 

