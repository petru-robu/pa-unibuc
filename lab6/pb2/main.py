import random

def inc_note(elevi, cnp):
    if cnp in elevi:
        elevi[cnp][2][0] += 1
    else:
        return None
        
def add_note(elevi, cnp, new_notes):
    if cnp in elevi:
        elevi[cnp][2].extend(new_notes)

def erase(elevi, cnp):
    if cnp in elevi:
        del elevi[cnp]

def cmp(x):
    nume, prenume, note = x[0], x[1], x[2]
    medie = sum(note)/len(note)
    return (-medie, nume, prenume)

def add_random_code(elevi):
    r1 = str(random.randrange(0, 10))
    r2 = str(random.randrange(0, 10))
    r3 = str(random.randrange(0, 10))
    l1 = chr(ord('a')+ random.randrange(0, 27))
    l2 = chr(ord('a')+ random.randrange(0, 27))
    l3 = chr(ord('a')+ random.randrange(0, 27))

    code = r1 + r2 + r3 + l1 + l2 + l3
    print(code)

if __name__ == '__main__':
    f = open('elevi.in', 'r')

    elevi = {}

    for line in f:
        elev = line.split()
        cnp = elev[0]
        nume = elev[1]
        prenume = elev[2]
        note = [int(x) for x in elev[3:]]
        elevi[cnp] = [nume, prenume, note]

    l = []
    for key in elevi:
        l.append(elevi[key])

    l.sort(key=cmp)
    #print(l)
    add_random_code(elevi)