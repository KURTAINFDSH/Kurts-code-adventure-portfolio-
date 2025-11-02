#data storage for student
students = []
age = []
birth_year = []

#loop for continues regestering
while True:
  
  print("\nWhat can i help?\n [1]Register\n [2]Student list")
  operation = input("")
  
  
#for registering
  if operation == '1':
    print("-----REGISTER-----")
    names = input("Name |: ").upper()
    ages = input("Age |: ")
    birth = input("Birthyear |: ")
    
    
    print(f"succesfully registered {names} {ages} {birth}")
    
    
#applying value to data 
    students.append(names)
    age.append(ages)
    birth_year.append(birth)
  
  
#if no student registered and student list
  elif operation == '2':

    if not students:
      print("no student has ben registered")
      
    else:
      print("student list")
      print("NAME----------------AGE--------BIRTHTYEAR")
      for i,students in enumerate(students):
        print(f"{students:<20}{age[i]:<12}{birth_year[i]}") 