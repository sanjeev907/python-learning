# class Employee:
#     company = "google"

#     def showdetails(self):
#         print("Hi Meenaskhi")
    
# class Programmer(Employee):
#     language = "Python Backend"
#     def getdetails(self):
#         print("Hi every python lover")

# e = Employee()
# e.showdetails()
# print(e.company)
# p = Programmer()
# print(p.company)

# Multiple inheritance


# class Employee:
#     company = "google"

    
# class Programmer:
#     language = "Python Backend"


# class Get(Employee, Programmer):
#     name = "Sanjeev"


# g = Get()
# print(g.company)


# class methods

# class Employee:
#     company = "Oodles Technologies"
#     salary = 100
#     location = "faridabad"

#     # def changesalary(self, sal):
#     #     self.salary = sal

#     @classmethod
#     def changesalary(cls, sal):
#         cls.salary = sal


# e = Employee()
# print(e.salary)
# print(e.company)
# e.changesalary(500)
# print(e.salary)

class Employee:
    company = "Oodles Technologies"
    salary = 100
    salarybonus = 200

    @property
    def Totalsalarybonus(self):
       return self.salary + self.salarybonus

e = Employee()
print(e.Totalsalarybonus)








