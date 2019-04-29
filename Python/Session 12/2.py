x = 1 #player x
y = 2 #player y
for i in range(4):
    for j in range(4):
        if i==y and j==x:
            print('P ' ,end='')
        elif i==1 and j==2:
            print('K ',end='')
        elif i==2 and j==3:
            print('E ',end='')
        else:
            print('- ',end='')
    print()

while True:
    move = input("Your movement: ").upper()

    # Control
    if move == 'W':
        y = y - 1
    if move == 'A':
        x = x - 1
    if move == 'S':
        y = y + 1
    if move == 'D':
        x = x + 1
    if y == -1:
        y = 0
    if x == -1:
        x = 0
    if y == 4:
        y = 3
    if x == 4:
        x = 3





    for i in range(4):
        for j in range(4):
            if i==y and j==x:
                print('P ' ,end='')
            elif i==1 and j==2:
                print('K ',end='')
            elif i==2 and j==3:
                print('E ',end='')
            else:
                print('- ',end='')
        print()