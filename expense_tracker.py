print("==Personal Expense tracker==")

expenses = []


def add_expense():
    name=input("Enter espense name:")
    amount=float(input("Enter amount :"))
    
    expense={                             "name":name,
         "amount":amount}
         
    expense.append(expense)
  
print(" Expense added successfully!")  

def show_expenses():
    print("==All Expenses==")

    if len(expenses)==0:
        print("no expenses found.") 
    else:
            
         for expense in expenses:
                print("name:",expense["name"],"amount :",expense["amount "])
                
def total_expense():
    total = 0
    
    
    for expense in expenses:
        total += expense[" amount "]
        
    print(" total expense:",total)
        

                        
while True: 
               
      print("==menu==")  
      print("1.add expense") 
      print("2.show expenses")
      print("3.total expense") 
      print("4.exit")
      
      choice=input("enter your choice:") 
      choice=input("enter expense name:")
      choice=input("enter amount :")
      
      if choice ==  "1" :
         add_expense()          
                        
      elif choice == "2" :
          show_expenses()
          
      elif choice =="3" :
          total_choice()           
     
      elif choice == "4" :
          print("thank you! ")
          break
          
      
      else:
          print(" Invalid choice")                                                          
