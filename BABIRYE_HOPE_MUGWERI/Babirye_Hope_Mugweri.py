#convert temperature 37 from celcius to fahrenheit
class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def cnovert_to_fahrenheit(self):
        temp1 = (self.temp * 9/5) + 32
        print(temp1)

new_temp = Temperature(37)
new_temp.cnovert_to_fahrenheit()

#Encapsulation
class Worker:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        print("WORKER'S DETAILS")

    def get_name(self):
        return self._name
    
    def get_salary(self):
        return self._salary
    
    def set_increment(self, new_salary):
        self._salary = new_salary

    def increase_salary(self, increased_salary):
        self._salary += increased_salary

employee = Worker("Hope", 850000)
print("NAME: ", employee.get_name())
print("CURRENT SALARY: ",employee.get_salary())
employee.set_increment(1000000)
print("NEW SALARY: ", employee.get_salary())