print("==Student Marks Analyzer==")


marks=[80,75,85,90,56,77,55]
print("Marks:",marks)

#Nambar of Students
total_students =len(marks)

print("total_students:",total_students)

#Total Marks
total_marks = sum(marks)

print("total_marks:",total_marks)

#Average
average = total_marks/total_students 

print("avrage marks:",average)

#Highest and Lowest
highest = max(marks)
lowest = min(marks)

print("highest marks:",highest)
print("lowest marks:",lowest)

#Pass and Fail

print("==Result==")

for mark in marks:
    if mark >=40:
        print(mark,"pass")
        
    else:
        print(mark,"fail")
        
    
