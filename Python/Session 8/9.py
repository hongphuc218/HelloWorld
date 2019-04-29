i = input('enter numbers: ')
listString = i.split(' ')
listInt = []
for l in listString:
  listInt.append(int(l))
print(*listInt)
print('Sum of all number: ', sum(listInt))
