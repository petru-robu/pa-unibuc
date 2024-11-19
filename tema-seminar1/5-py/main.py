# O(log)
def count_bits(x):
    cnt = 0
    while x:
        if x%2 == 1:
            cnt+=1
        x//=2
    return cnt

if __name__ == '__main__':
    x = int(input())
    cx = x

    log = 0
    while x:
        log += 1
        x//=2

    print(log - count_bits(cx))

