
if __name__ == "__main__":
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    if (a <= 0 or a >= 24 or b <= 0 
        or b >= 60 or c<=0 or c>=60):
        print("Eroare, format incorect!")
    else:
        print(f"Ora este {a}:{b}:{c}")