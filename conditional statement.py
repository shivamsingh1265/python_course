# if statement.

age = 17
if (age >= 18):
    print("can vote and apply for licence")
    
# elif statement.
 
light = "pink"
if (light == "red"):    
    print("stop")               #indentation
elif (light == "green"):
    print("go")
elif (light == "yellow"):
    print("look")
else:
    print("light is brokrn")
    
print("end of code")   


marks = int (input("enter student marks:"))
if (marks >= 90):
     grade = "A"
elif (marks >= 80 and marks < 90):
    grade ="B"   
elif (marks >= 70 and marks < 90):
    grade ="C"
else :
    grade ="D"
    
print("grade of the student ->", grade)        

 #nesting
age = 82
if (age >= 18):
    if (age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
    
    