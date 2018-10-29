while True:
  print('''How many legs does a spider have?
1. None
2. 4 legs
3. 8 legs
4. 12 legs''')
  answer = (input("enter your answer"))
  if answer.isdigit() == True:
    if int(answer) == 3:
      print("correct")
      break
    else:
      print("wrong")
  else:
    print("wrong")