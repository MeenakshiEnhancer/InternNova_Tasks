mark=float(input("Enter mark:"))

if(mark<0 or mark>100):
  print("Invalid Marks! please enter mrks between 0 and 100")
else:
  if(mark>=90):
    print("A")
  elif(75<=mark<=89):
    print("B")
  elif(60<=mark<=74):
    print("C")
  else:
    print("fail")