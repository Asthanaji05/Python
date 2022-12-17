import math
print("OM GAN GANPATAYE NAMAH")
print("Jai Shree Ram\n")
print("Game Begins - \n")

#Python Program Start
#addition
def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def average(num1,num2):
    return (num1+num2)/2
def division(num1,num2):
    return num1/num2   
def sin(num1):
    return math.sin(num1)
def sin(num2):
    return math.sin(num2)

print("Select any operation you want- \n" \
  "1.Addition- \n"
  "2.Substraction - \n"
  "3.multiplication- \n"
  "4.Average- \n" 
  "5.division - \n"
  "6. Sin- \n"
  "7. Cos- \n"
  "8. Tan- \n")

select = int(input("select operation from 1,2,3,4,5,6,7 :  "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
if select == 1:
    print(num1,"+",num2,"=" ,addition(num1,num2) )
elif select == 2:
    print(num1,"-",num2,"=" ,subtraction(num1,num2) )
elif select == 3:
    print(num1,"x",num2,"=" ,multiplication(num1,num2) )
elif select == 4:
    print(num1,"+",num2,"/2","=" ,average(num1,num2) )
elif select == 5:
    print(num1,"/",num2,"=" ,division(num1,num2) )
elif select == 6:
    print(math.sin(num1))
    print(math.sin(num2))
elif select == 7:
    print(math.cos(num1))
    print(math.cos(num2))
elif select == 8:
    print(math.tan(num1))
    print(math.tan(num2))
else:
    print("Invalid input")
