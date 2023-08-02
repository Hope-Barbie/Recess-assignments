class Salary:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calc_bonus(self,):
        self.bonus = (self.salary * 0.15)
        print(self.name, "has a salary of",self.salary, "and a bonus of", self.bonus)

employee = Salary("Hope", 150000)
print(employee.calc_bonus)