student_details={ }
def add_student(name,grade):
    student_details[name]=grade
    print(f"added {name} with grade {grade}")

def update_student(name,grade):
    if name in student_details:
        student_details[name]=grade
        print(f"updated {name} with grade {grade}")
    else:print("student {name} not found")

def delete_student(name):
    if name in student_details:
      del student_details[name]
    print(f"student {name} is deleted sucessfully")


def display_all_students():
    if student_details:
     for name, grade in student_details.items():
        print(f"{name} : {grade}")
    else:print("student not found")


while True: 
      print("\n student grade management system")
      print("1. Add student ")
      print("2. update student")
      print("3. delete student")
      print("4. view all students")
      print("5. Exit")

      choice=input("select the choice : ")
      if choice=="1":
         name=input("enter the name : ")
         grade=int(input("enter the grade : "))
         add_student(name,grade)
      elif choice=="2":
         name=input("enter the name : ")
         grade=int(input("enter the grade :"))
         update_student(name,grade)
      elif choice=="3":
         name=input("enter the name : ")
         delete_student(name)
      elif choice=="4":
         display_all_students()
      elif choice=="5":
         print("program closed")
         break
      else:
         print("Invalid input")


    