print("Sales Data Analyzer")


sales=[{"product":"laptop","price":6000,"quantity":2},{"product":"phone","price":3000,"quantity":3},{"product":"headphone","price":3000,"quantity":5},{"product":"keyboard","price":2000,"quantity":4}]


def show_sales():
    print("===All sales===")
    for sale in sales:
        total=sale["price"]*sale["quantity"]
        print(" product:",sale["product"],"|price:",sale["price"],"quantity:",sale["quantity"],"total:",total)
        
        
        
                
def total_sales():
    total=0
    for sale in sales:
        total += sale["price"]*sale["quantity"] 
        print("total sales:",total)  
        
           
def highest_sale():
    highest=0
    product=""  
    for sale in sales:
        total=sale["price"]* sale["quantity"]
        if total > highest:
            highest = total
            product =sale["product"]  
            
                     
        print("highest sale:",product )
        print("amount:",highest ) 
        
                                     
def average_sale():
    total=0
    
    for sale in sales :
        total+=sale["price"]*sale["quantity"]
        average = total/len(sales)
        print("average sale:",average )
        
 
while True:
    
    
    print("===Menu===")
    print("1.show sales")
    print("2.total sales")
    print("3.highest sale")
    print("4.average sale")
    print("5.exit")
    
    
    
    choice=input("enter your choice:") 
    
    
    if choice=="1":
        show_sales() 
   
    elif choice=="2":
          total_sales()  
          
    
    elif choice=="3":
          highest_sale() 
          
      
    elif choice=="4":
          average_sale()


    elif choice=="5":
         print("Thank you!")
         break
         
         
    else:
         print("Invalid choice ")
