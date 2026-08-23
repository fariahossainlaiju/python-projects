print("==Students Management Systems ==")

students={}

def add_student():
    name=input("enter student name:")
    age=int(input("enter student age:"))
    marks=float(input("enter student marks:"))
    

    students[name]={                     "age":age,                       "marks":marks            }

print("student added successfully") 


def show_students():
   if len(students)==0:
       print(" no students found.")
    
   else:
        print("==All Students==")
        
        
        for name,info in students.items():
            print("Name:",name)
            print("Age:",info["age"])
            print("marks:",info["marks"])
            print("------------")
            
   
def search_student():
    print("student not found!") 
    print("name:",name)  
    print("age:",students[name]["age"])
    print("marks:",students[name]["marks"])
    
    print("student not found.")
    
    
    
while True:
    
        print("===MENU===") 
        print("1.Add student")
        print("2.Show students")
        print("3.Search student") 
        print("4.Exit")  
        
        
        choice = input("Enter your choice:")
        if choice =="1":
            add_student()
            
        elif choice =="2":
            show_students()
            
        
        elif choice =="3":
            search_student()       
    
        elif choice =="4":
            print("program finished.")
            break
             
        else:
             print("Invalid choice!")
