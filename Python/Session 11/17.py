computer = {
  'HP':20,
  'DELL':50,
  'MACBOOK':12,
  'ASUS':30,
}
computer['FUJITSU']=15
computer['ALIENWARE']=5
export = input('computer name ?')
num = int(input('Number of computers'))
computer[export] = computer[export]-num
print(export, ':', num)
print(computer)