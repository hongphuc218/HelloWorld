player = {
"name": "Faker",
"age": 22,
"height": "1.76m",
"team": "SKTT1",

}
print(player)
key = input("key?")
value = input("value?")
player[key] = value
print(player)
o = input("key_to_del")
del player[o]
print(player)