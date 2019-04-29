computer = {
  'HP':20,
  'DELL':50,
  'MACBOOK':12,
  'ASUS':30,
  'FUJITSU':15,
  'ALIENWARE':5,
}

price = {
  'HP':600,
  'DELL':650,
  'MACBOOK':12000,
  'ASUS':400,
  'FUJITSU':900,
  'ALIENWARE':1000,
}
total={}
for key,value in computer.items():
  for key1,value1 in price.items():
    if key == key1:
      total[key]=value*value1
print(total)
for i in total:
    print(i)    