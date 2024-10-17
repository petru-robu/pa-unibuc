
if __name__ == "__main__":
    s = input()
    a, b, p = input().split()
    p = int(p)

    cnt = 0
    while s.find(a):
        cnt += 1
    
    if cnt > p:
        print("Prea multe greseli de corectat, au fost corectate p")

    s = s.replace(a, b, p)
    print(s)