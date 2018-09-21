def game_rules(x,y):
    position = (x,y)
    if position == (1, 1):
        print("You can travel: (N)orth.")
        newpos = check_input("nN",position)
    elif position == (1, 2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        newpos = check_input("NnEeSs",position)
    elif position == (1, 3): 
        print("You can travel: (E)ast or (S)outh.")
        newpos = check_input("EeSs", position)
    elif position == (2, 1): 
        print("You can travel: (N)orth.")
        newpos = check_input("Nn", position)
    elif position == (2, 2):
        print("You can travel: (S)outh or (W)est.")
        newpos = check_input("SsWw", position)
    elif position == (2, 3): 
        print("You can travel: (E)ast or (W)est.")
        newpos = check_input("EeWw", position)
    elif position == (3, 2):
        print("You can travel: (N)orth or (S)outh.")
        newpos = check_input("NnSs", position)
    elif position == (3, 3):
        print("You can travel: (S)outh or (W)est.")
        newpos = check_input("SsWw", position)
    return newpos

def check_input(m,position):
    valid_input= str(input("Direction: "))
    if not valid_input in m:
        print("Not a valid direction!")
    else:
        #kalla check fall  
        xx = pos[0]
        yy = pos[1]

        if valid_input == "N" or valid_input == "n":
            yy += 1
        elif valid_input == "S" or valid_input == "s":
            yy -= 1
        elif valid_input == "E" or valid_input == "e":
            xx += 1
        elif valid_input == "W" or valid_input == "w":
            xx -= 1

    return (xx,yy)

x = 1
y = 1
pos=(1,1)
victory = False 

while not victory:
    pos = game_rules(x,y)
    x = pos[0]
    y = pos[1]
    if x == 3 and y == 1:
        print("Victory")
        victory = True




    

