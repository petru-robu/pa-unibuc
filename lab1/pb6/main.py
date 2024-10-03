maxdiff = -1
zi = -1

curs = input().split(',')
for i in range(len(curs)):
    curs[i] = float(curs[i])

for i in range(len(curs)-1):
    diff = curs[i] - curs[i+1]
    diff *= -1
    if(diff > maxdiff):
        maxdiff = diff
        zi = i

maxdiff = round(maxdiff, 2)
print(f"Cea mai mare crestere a fost de {maxdiff}, intre zilele {i} si {i+1}")