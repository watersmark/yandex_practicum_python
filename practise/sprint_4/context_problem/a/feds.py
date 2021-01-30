class Temp:

    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_elem(self, value):
        self.age = value


if __name__ == "__main__":

    # mass_elem = [Temp(32), Temp(45), Temp(65)]
    # for elem in mass_elem:
    #     elem.set_elem(100)
    #
    # for elem in mass_elem:
    #     print(elem.get_age())

    mass = [1, 3, 4]

    for index in range(len(mass)):
        mass[index] = 32

    for elem in mass:
        print(elem)
    