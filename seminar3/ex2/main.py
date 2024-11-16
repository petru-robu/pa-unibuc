def anagrams(s1, s2):
    map = {}
    for ch in s1:
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] += 1
    for ch in s2:
        if ch not in map:
            return False
        else:
            map[ch] -= 1

    for key in map:
        if map[key] != 0:
            return False
        
    return True


def permutations(s, t):
    if not anagrams(s, t):
        return None
    
    p = {pos:pos for pos in range(0, len(s)+1)}
    q = {pos:pos for pos in range(0, len(s)+1)}

    s_copy = s
    for i in range(len(t)):
        pos = s.find(t[i])

        s = list(s)
        s[pos] = '#'
        s = ''.join(s)
        
        p[i+1] = pos+1

    s = s_copy
    for i in range(len(s)):
        pos = t.find(s[i])

        t = list(t)
        t[pos] = '#'
        t = ''.join(t)
        
        q[i+1] = pos+1

    return [p, q]

if __name__ == '__main__':
    s = 'treime'
    t = 'emerit'

    perm = permutations(s, t)

    for key in perm[0]:
        print(perm[0][key], end=' ')

    print()

    for key in perm[1]:
        print(perm[1][key], end=' ')