print("==Student Information==")

student={             "name":"faria",          "age":23,  "country":"bangladesh",         "course":"python",      "marks":85                       }

print("name:",student["name"])
print("age:",student["age"])
print("country:",student["country"])
print("course:",student["course"])
print("marks:",student["marks"])



print("==Update Information==")

student["marks"]=90
student["city"]="comilla"

print(student)
