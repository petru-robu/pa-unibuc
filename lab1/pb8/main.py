v = input().split()
for i in range(len(v)):
    v[i] = int(v[i])
v.sort()

print(f"Diferenta este {v[2] - v[0]}")
