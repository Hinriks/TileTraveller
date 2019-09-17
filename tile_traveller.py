""" 
tvö variables, x og y, sem fer frá 1 upp í 3 (sem myndar 3x3 grid). 
staðsetning leikmans er x,y og kemst ekki út fyrir 3x3 gridið (athuga með if statement).
Leikmaður getur farið á milli reita nema þegar það er lokaður veggur í þá átt sem hann vill fara (athuga með if statement). 
Leikmaður byrjar á reit 1,1 og vinnur leikinn á reit 3,1.
"""

x_pos = 1
y_pos = 1


"""def position_checker(x, y):

    if y == 1:
        y += 1
    elif y == 2:
        if x == 2:
            x -= 1
            y -= 1
        elif x == 3:
            y += 1
            y -= 1
    elif y == 3:
        if x== 2:
            x += 1 
            x -= 1
    """


def check_victory(x, y):
    if x == 3 and y == 1:
        return True
    else:
        return False

def grid_border_checker(x, y):
    if x > 3:
        x = 3
        print ("Not a valid direction!")
    elif x < 1:
        x = 1
        print ("Not a valid direction!")
    if y > 3:
        y = 3
        print ("Not a valid direction!")
    elif y < 1:
        y = 1
        print ("Not a valid direction!")
    
    return x,y

def grid_wall_checker(x, y):
    """if y == 1:
        
    elif y == 2:
        if x == 2:
            x -= 1
            y -= 1
        elif x == 3:
            y += 1
            y -= 1
    elif y == 3:
        if x== 2:
            x += 1 
            x -= 1"""

def invalid_direction():
    print("Not a valid direction!")

west = True
east = True
south = True
north = True

def allowed_movements(x, y, w, e, s, n):
    print ("You can travel: ", end="")
    if x > 1:
        if x == 3 and y == 2:
            w = False
        elif x == 3 and y == 1:
            w = False
        elif x == 2 and y == 1:
            w = False
        else:
            print("(W)est", end=" ")
    else:
        w = False
    if x < 3:
        if x == 1 and y == 1:
            e = False
        elif x == 2 and y == 1:
            e = False
        elif x == 2 and y == 2:
            e = False
        else:
            print("(E)ast", end=" ")
    else:
        e = False
    if y > 1:
        if x == 2 and y == 3:
            s = False
        else:
            print("(S)outh", end=" ")
    else:
        s = False
    if y < 3:
        if x == 2 and y == 2:
            n = False
        else:
            print("(N)orth", end=" ")
    else:
        n = False
    print (".")

    return w,e,s,n

while True:
    west,east,south,north = allowed_movements(x_pos, y_pos, west, east, south, north)

    user_input = input("Direction: ")
    if user_input == "n" and north:
        y_pos += 1
    elif user_input == "e" and east:
        x_pos += 1
    elif user_input == "s" and south:
        y_pos -= 1
    elif user_input == "w" and west:
        x_pos -= 1
    else:
        invalid_direction()

    x_pos, y_pos = grid_border_checker(x_pos, y_pos)


    if check_victory(x_pos, y_pos):
        print ("Victory!")
    
    west,east,south,north = True,True,True,True



"""while available position is entered
    change position
    if not do not change position and print unavailable"""