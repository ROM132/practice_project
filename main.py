class Student:

    money_amount = "Enter how much dollar you have?: "
    debt_amount = "Enter how much you owe?: "

    def __init__(self, name, major, grade_major):
        self.name = name
        self.major = major
        self.grade_major = grade_major
        self.qus = None

    def money_handler(self):
        self.qus = input("You in (d)debt or in (p)plus? in you bank account?: ")
        if self.qus == "p":
            s.plus_money()

        elif self.qus == "d":
            s.minus_money()

        else:
            print("That not an option! try again!")

    def plus_money(self):
        s.int_convert(self.money_amount)
        s.plus_minus_checker()

    def minus_money(self):
        s.int_convert(self.debt_amount)
        s.plus_minus_checker()

    def int_convert(self, i):
        i = i
        i1 = i
        while True:
            i = input(i)
            if i.isdigit():
                i = int(i)
                self.money_amount = i
                self.debt_amount = i
                break
            else:
                print("Pick an number next time!")
                i = i1
                continue

    def plus_minus_checker(self):
        if self.qus == "p":
            print(f"{self.name} i see you are in plus of: {self.money_amount} dollar!")
        elif self.qus == "d":
            print(f"{self.name} i see you are in debt of: {self.money_amount} dollar!")
        else:
            print("Rom you have an error!")


s = Student("rom", "programmer", 74)
s.money_handler()
