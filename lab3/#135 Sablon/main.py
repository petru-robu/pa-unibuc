
if __name__ == '__main__':

    s1, s2 = input().split()
    sablon=''
    voc = 'aeiou'

    if len(s1) != len(s2):
        print("Nu exista sablon!")
        exit(0)
    
    for i in range(len(s1)):
        
        if s1[i].isalpha() and s2[i].isalpha():
            a = (voc.find(s1[i]) >= 0)
            b = (voc.find(s2[i]) >= 0) 
            
            if (not a) and (not b):
                sablon += '#'
            elif a and b:
                sablon += '*'
            elif a != b:
                sablon += '?'
        else:
            sablon += '?'

    print(sablon)

