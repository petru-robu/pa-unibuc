def count_bits(x):
    cnt = 0
    while x:
        if x%2 == 1:
            cnt+=1
        x//=2
    return cnt

if __name__ == "__main__":

    x, y = input().split()
    x = int(x)
    y = int(y)

    t = x ^ y
    print(count_bits(t))