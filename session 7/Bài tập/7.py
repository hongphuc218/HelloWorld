favorite = ['LOL', 'sport', 'BTS', 'Game']
print(favorite)
newfav = input("new favorite")
favorite.append(newfav)
print(favorite)
print(*favorite, sep=' | ' )