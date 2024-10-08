
class Flower:
    def __init__(self, name, pedals_no, price):
        self.__name = name
        self.__pedals_no = pedals_no
        self.__price = price
    
    def set_price(self, price):
        self.__price = price
    def set_pedals_no(self, pedals_no):
        self.__pedals_no = pedals_no   
    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price
    def get_pedals_no(self):
        return self.__pedals_no
    def get_name(self):
        return self.__name
    
if __name__ == "__main__":
    F = Flower("zambila", 12, 21.5)
    print(F.get_name())
    print(F.get_pedals_no())
    print(F.get_price())

    F.set_price(34.5)
    print(F.__price)