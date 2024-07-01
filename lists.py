#lists allow us to store a sequence of items in a single variable.
 
ages = [19, 26, 23]
print(ages)

student = ["ram","shyam","geeta" ]
print(student)
#using list to create list
x = "abc"
result = list(x)
print(result)

#remove from list item
numbers = [2,4,6,8,10]
numbers.remove(4)
print(numbers)

#add element to a list
fruits = ["apple", "banana", "pineapple", "mango"]
print('Original List:', fruits)

# using append method to add item in list
fruits.append('cherry')
print('Updated List:', fruits)

fruits = ["apple","banana", "papaya","apple"]    #duplicate are allowed
print(fruits)

colors = ['Red', 'Black', 'Green']
print('Original List:', colors)
colors[2] = 'Blue'
print('Updated List:', colors)

