w = int(input('enter width'))
h = int(input('enter height'))
x = int(input('enter coordinate x'))
y = int(input('enter coordinate y'))
for i in range(h):
    for j in range(w):
        if i==y-1 and j==x-1:
            print('x ',end='')
        else:
            print('- ',end='')
    print()