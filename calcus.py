#for op to work

def multiply(a, b):
  return a * b

def add(a, b):
  return a + b
  
def division(a, b):
  return a / b
  
def subtraction(a, b):
  return a * b
  
#input & result
  
a = int(input("number1: "))
b = int(input("number2: "))

op = input("operation: ")

#to what op to use

if op == "multiply":
  result = multiply(a, b)

elif op == "add":
  result = add(a, b)
  
elif op == "division":
  result = division(a, b)
  
elif op == "division":
  result = subtraction(a, b)

print(result)