# def meassge():
#     print("hello python")
# meassge()
# meassge()

# def function():
#     print("good day bye bye everyone")
  
# function()


# Recussion
i=0

def myfun():
    global i
    i=i+1
    print("Hello sanjeev kaushik", i)
    myfun()

myfun()

# practice set 

# Q1

# def max(num1,num2,num3):
#     if(num1>num2):
#         print("num1 is greater than num2")
#     elif(num2>num3):
#         print("num2 is greater than num3")
#     else:
#         print("num3 is smaller than everyone")

# m=max(10,8,20)
# print("the value of max" + str(m))