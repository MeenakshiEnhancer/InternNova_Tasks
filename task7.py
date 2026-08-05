#String operations :upper(), lower(), replace(), find()
word="Python Programming"

print("Upper Case:",word.upper())
print("Lower Case:",word.lower())

old_word="Python"
new_word="Java"
print(word.replace(old_word,new_word))
search=word.find('gram')

#List operations (append(), remove(), sort())
lst=list(map(int,input("Enter numbers separated by spaces ").split()))
print("original list:",lst)
lst.append(36)
print("After append: ",lst)
lst.remove(36)
print("After removal:",lst)
lst.sort()
print("After sorting",lst)

#Tuple creation and indexing

# Tuple Creation and Indexing

tup = ("Apple",1, True, 10.5, 9)

print("Tuple:", tup)

print("First Element :", tup[0])
print("Second Element:", tup[1])
print("Last Element  :", tup[-1])

#Dictionary storing student information

student={"name":"Meera",
      "rollNo":101,
      "college":"JNTUA",
      "department" :"ECE"}
print(student)
print("----student Information----")
print("Name: ",student["name"])
print("Roll no:",student["rollNo"])
print("College:",student["college"])
print("Department:",student["department"])


#Set operations (add(), remove())

data = {101, "Meera", 9.23, True,1}

print("Original Set:", data)

data.add("Python")
print("After add:", data)

data.remove(9.23)
print("After remove:", data)
