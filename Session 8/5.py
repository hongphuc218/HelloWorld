color = ['red', 'green', 'blue']
print('Our color list:')
for i,item in enumerate(color):
  print(i+1,'.',item)
Del = input('Item to delete: ')
if Del.isdigit():
  color.pop(int(Del))
else:
  color.remove(Del)
for i,item in enumerate(color):
  print(i+1,'.',item)
