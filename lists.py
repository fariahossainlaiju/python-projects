print("==Student Marks ==")


marks=[78,70,95,55,76]

print("Marks:",marks)

print("First mark:",marks[0])
print("Last mark:",marks[-1])

print("Number Of Student :",len(marks))

print("Total Marks :",sum(marks))

print("Highest Marks:",max(marks))

print("Lowest Marks:",min(marks))




print("==Add New Marks==")

marks.append(88)

print("update marks:",marks)



print("==Remove Marks==")

marks.remove(55)

print("After Removeing:",marks)


print("==Sorted Marks==")

marks.sort()

print("Ascending:",marks)



print("===All Marks===")

for mark in marks:
    print("mark:",mark)
