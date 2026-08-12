print("==Simple Function==")



def welcome():
    print("welcome to python ")
    print(" Let's Learn function  ")
    
welcome()


print("==Function With Parameter==")


def greet(name):
    print(" hello",name)
    
    
greet("faria")
greet("rahim")


print("==Tow Parameters==")


def student(name,age):
    print("name:",name)
    print("age:",age)

student("faria",23)


print("==User Input Function ==")


def Info(name,country):
    print("name:",name)
    print("country:",country)
    
    
name=input("Enter your name:")
country=input("Enter your country:")  

  
      
Info(name,country)


print("==Return Function ==")


def add(a,b):
    return a+b
result =add(20,70)

    
print("Total:",result)  

          
print("==Calculator ==") 

def add(a,b):
    return (a+b)                      
                                                           
def sub(a,b):
    return (a-b)
    
x=int(input("Enter first nambar :"))
y=int(input("Enter second nambar :"))

print("Addition:",add(x,y))     
print("Subtraction:",sub(x,y))                                
