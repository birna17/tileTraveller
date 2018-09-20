#Which implementation was easier and why ?
#Which implementatio is more readable and why ?
#Which problems in the first impolementations were you able to solve with the later implementation?
  

x = 1
y = 1
valid_direction = "nN"
victory = False
print("You can travel: (N)orth.")

position = (x,y)
def coord_moves(x,y):
    """Defines which way you will travel depending on your input"""
    x=1
    y=1
    if move == "n" or move == "N":
        y += 1
    elif move == "s" or move == "S":
        y -= 1
    elif move == "e" or move == "E":
        x += 1
    else: 
        x -= 1
   
    
def game_rules(valid_direction):
    """All possible outcomes from player's moves, under surtain conditions"""
    if position == (1, 1):
        valid_direction = "nN" 
        print("You can travel: (N)orth.")
    elif position == (1, 2):
        valid_direction= "nNeEsS"
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif position == (1, 3):
        valid_direction= "eEsS" 
        print("You can travel: (E)ast or (S)outh.")
    elif position == (2, 1):
        valid_direction= "nN" 
        print("You can travel: (N)orth.")
    elif position == (2, 2):
        valid_direction= "wWsS"
        print("You can travel: (S)outh or (W)est.")
    elif position == (2, 3): 
        valid_direction= "eEwW"
        print("You can travel: (E)ast or (W)est.")
    elif position == (3, 1):
        print("Victory!")
        victory = True
    elif position == (3, 2):
        valid_direction= "nNsS" 
        print("You can travel: (N)orth or (S)outh.")
    elif position == (3, 3):
        valid_direction= "sSwW"
        print("You can travel: (S)outh or (W)est.")





while not victory:
    direction = input("Direction: ")
    if not direction in valid_direction: 
        print("Not a valid direction!")
    else:
        coord_moves(direction)
        game_rules(valid_direction)