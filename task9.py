# Mini Project
# Student Management System

students=[]

def add_student():
   name=input("Enter Name: ")
   rollNo=input("Enter roll no:")
   age=input("Enter age:")
   college=input("Enter college name:")
   branch=input("Enter branch: ")

   data={"Name":name,
         "rollNo":rollNo,
         "Age":age,
         "College":college,
         "Branch":branch
    }
   students.append(data)
   print("Added student info successfully")

    
def display_info():
   if(len(students)==0):
        print("No record found")

   else:
       print("------Students Records----- ")
       for student in students:
         print("name :",student["Name"])
         print("roll no:",student["rollNo"])
         print("Age: ",student["Age"])
         print("College: ",student["College"])
         print("branch:",student["Branch"])
         print("-------------")

def searchStudent():
   std_name=input("Enter student name to fetch details: ")
   for student in students:
      if std_name.lower()==student["Name"].lower():
         print("Record found!")
         print("Name:",student["Name"])
         print("roll no:",student["rollNo"])
         print("Age: ",student["Age"])
         print("College: ",student["College"])
         print("branch:",student["Branch"])
         return
      else:
         print("Record not found")


def delete_student():
   name=input("Enter student name to delete:")

   for student in students:
      if student["Name"].lower()==name.lower():
         students.remove(student)
         print("Removed data")
         return

   else:
      print("Student not found")


while True:
   print("=======Student Management System======")
   print("1.Add Student")
   print("2.Display Students")
   print("3.Search Student")
   print("4.Delete Student")
   print("5.Exit")
   choice=int(input("Enter your choice: "))

   if choice==1:
     add_student()
   elif choice==2:
     display_info()
   elif choice==3:
     searchStudent()
   elif choice==4:
     delete_student()
   elif choice==5:
     print("Thank you")
     break
   else:
     print("Invalid choice.Please try again")