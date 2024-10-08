

class Vector:
    def __init__(self, l):
        self.v = l

    def __len__(self):
        return len(self.v)

    def __getitem__(self, i):
        return self.v[i]
    
    def __setitem__(self, j, val):
        self.v[j] = val

    def __add__(self, vec):
        if len(self) != len(vec):
            raise ValueError("Diffrent Dimensions!")
        
        result = Vector(len(self) * [0])

        for i in range(len(self)):
            result[i] = self[i] + vec[i]
        
        return result
    
    def __sub__(self, vec):
        if len(self) != len(vec):
            raise ValueError("Diffrent Dimensions!")
        
        result = Vector(len(self) * [0])

        for i in range(len(self)):
            result[i] = self[i] - vec[i]
        
        return result

    def __eq__(self, other):
        return self.v == other.v
    
    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self.v)[1:-1] + '>'
    

if __name__ == "__main__":

    v1 = Vector([12, 3, 4])
    v2 = Vector([0, 1, 0])

    v3 = [3, 0, 3] + v1 
    print(v3)