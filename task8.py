#Basic File Handling 

with open("introduction.txt", "w") as file:
    file.write("My name is Meenakshi Muthukumaran.\n")
    file.write("I am interested in Python programming and Data Analytics.\n")
    file.write("I enjoy learning new concepts and working on real-world projects.\n")
    file.write("I am eager to develop my skills and grow as a professional.")

file.close()

# Reading the file
file = open("introduction.txt", "r")

content = file.read()

print("File Contents:\n")
print(content)

file.close()