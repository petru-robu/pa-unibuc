t = float(input())
v = input().split()

for i in range(len(v)):
    v[i] = float(v[i])

s = 0
d = 0
for i in range(len(v)):
    s += v[i]
    if(s > t):
        d = i
s = 0
for i in range(len(v)):
    s += v[i]
s /= len(v)

print(f"In ziua {d} se cumpara jucaria")
print(f"Se strang {round(s, 2)} bani pe zi in medie")