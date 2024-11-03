
def palindrom(s):
    rev = s[::-1]
    return (rev == s)

if __name__ == '__main__':
    
    s = input()

    pre, prepal ='',''
    for c in s:
        pre+=c
        if palindrom(pre):
            prepal = pre

    suf, sufpal = '', ''

    s = s[::-1]
    for c in s:
        suf+=c
        if palindrom(suf):
            sufpal = suf
    
    print(prepal, sufpal)