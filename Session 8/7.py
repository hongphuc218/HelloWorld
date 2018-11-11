list_ = [5,11,13,29,7]
l= int(input('Enter a number: '))
flag = False
position = -99999
for i,item in enumerate(list_):
  if l == item:
    position = i
    flag = True

if flag == True:
  print("Found, position",position+1)
else:
  print('Not Found')