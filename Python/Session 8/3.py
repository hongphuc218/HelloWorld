color = ['red', 'green', 'blue']
print(color)
addcolor = input('new color?')
color.append(addcolor)
print("Our color list")
print(*color, sep=', ')