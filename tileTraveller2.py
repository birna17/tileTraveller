#Which implementation was easier and why ?
#Which implementatio is more readable and why ?
#Which problems in the first impolementations were you able to solve with the later implementation?


x = 1
y = 1
valid_direction = "nN"
victory = False
print("You can travel: (N)orth.")

position = (x,y)
def check(move,x,y):
    """Defines which way you will travel depending on your input"""
    if move == "n" or move == "N":
        y += 1
    elif move == "s" or move == "S":
        y -= 1
    elif move == "e" or move == "E":
        x += 1
    else: 
        x -= 1
   
    
def game_rules(v):
    """All possible outcomes from player's moves, under surtain conditions"""
    
    if position == (1, 1):
        v = "nN" 
        print("You can travel: (N)orth.")
    elif position == (1, 2):
        v = "nNeEsS"
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif position == (1, 3):
        v = "eEsS" 
        print("You can travel: (E)ast or (S)outh.")
    elif position == (2, 1):
        v = "nN" 
        print("You can travel: (N)orth.")
    elif position == (2, 2):
        v = "wWsS"
        print("You can travel: (S)outh or (W)est.")
    elif position == (2, 3): 
        v = "eEwW"
        print("You can travel: (E)ast or (W)est.")
    elif position == (3, 2):
        v = "nNsS" 
        print("You can travel: (N)orth or (S)outh.")
    elif position == (3, 3):
        v = "sSwW"
        print("You can travel: (S)outh or (W)est.")
# elif position == (3, 1):
        #print("Victory!")
        #victory = True
