import sys

if __name__ == "__main__":
    z, l, a = input().split('.')
    z = int(z)
    l = int(l)
    a = int(a)

    print(f"Ziua curenta: {z}/{l}/{a}")

    bisect = False
    if ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0):
        bisect = True

    if(z <= 0 or z >= 32 or l <= 0 or l>=12 or a<=0):
        print("Format incorect!")
        sys.exit(0)

    if(l % 2 == 1):
        if(z < 31):
            z+=1
        else:
            if(l < 12):
                l += 1
                z = 1
            else:
                a += 1
                l = 1
                z = 1
    else:
        md = 30
        if(l == 2):
            if(bisect):
                md = 29
            else:
                md = 28
        if(z < md):
            z+=1
        else:
            if(l <= 12):
                l += 1
                z = 1
            else:
                a += 1
                l = 1
                z = 1
    
    print(f"Urmatoarea zi: {z}/{l}/{a}")
                
                

    

    
        
    
