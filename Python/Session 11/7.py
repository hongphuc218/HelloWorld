computer = {
  'HP':20,
  'DELL':50,
  'MACBOOK':12,
  'ASUS':30,
}
i = input('add computer?')
y = input('number of PC?')
computer[i]=y
for key, value in computer.items():
  print(key, ":", value)
