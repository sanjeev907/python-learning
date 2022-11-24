# class Employee:
#     company = "Google"
#     def getSalary(self):
#         print("Salary is not there")

        
# sanjeev = Employee()
# sanjeev.getSalary()
 
# @staticmethod
# def greet():
#     print("hello everyone")
    
# greet()

# constructor

# class Employee:
#     def __init__(self):
#         print("Hello sanjeev kaushik welcome here")
#         sanjeev = Employee("sanjeev")

# Q1
# class Programmer:
#     company = "microsoft"
#     def __init__(self, name, product):
#             self.name = name
#             self.product = product
#     def getInfo(self):
#           print(f"The programmer name {self.name} and the product {self.product}")

# sanjeev = Programmer("sanjeev", "boat headphone")
# sanjeev.getInfo()




# Q2

# class Calcultor:
#     def __init__(self, num):
#         self.number = num
    
#     def square(self):
#         print(f"the value of {self.number} the square of {self.number **2}")
        
#     def squareRoot(self):
#         print(f"the value of {self.number} the square of {self.number **0.5}")

#     def cube(self):
#         print(f"the value of {self.number} the square of {self.number **3}")


#     a = Calcultor(3)
#     a.square()
#     a.squareRoot()
#     a.cube()

# Q5

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"the name of the is {self.name}")
        print(f"the name of the is {self.fare}")
        print(f"the name of the is {self.seats}")
intercity = Train("Intercity Express: 14555", 90, 300)

intercity.getStatus()