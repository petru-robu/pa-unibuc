
class Student:
    def __init__(self, nume, grupa, note):
        self.nume = nume
        self.grupa = grupa
        self.note = note
        self.promovat = self.promovat()

    def promovat(self):
        s = 0
        for nota in self.note:
            if nota == 0:
                return False
            s += nota

        if s < 5:
            return False
        return True
    
    def __repr__(self):
        return repr((self.nume, self.grupa, self.note, self.promovat))
        
def cmp(x):
    return (x.grupa, not x.promovat, x.nume)


if __name__ == '__main__':
    l = []

    l.append(Student('Petru', 152, [2, 4, 5, 1]))
    l.append(Student('Ionescu', 151, [2, 17, 3, 1]))
    l.append(Student('Ana', 152, [1, 0, 3]))

    l.sort(key=cmp)
    print(l)

    

