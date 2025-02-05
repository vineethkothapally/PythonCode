class Mammels:
    def Sounds(self):
        print("Innocent")


class Monkey(Mammels):
    def monkey(self):
        print("Devine")
class Dog(Mammels):
    def dog(self):
        print("loyal")

Animal1 = Dog()
Animal1.dog()
Animal1.Sounds()
Animal2 = Monkey()
Animal2.monkey()
Animal2.Sounds()