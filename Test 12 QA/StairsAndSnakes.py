import random


"""
input: 
stairs: A list to save the stairs that there are going to be in the board
pos: the current position of the player
output:
The new position of the player and it prints the action thas has been done
"""
def checkStairs(stairs, pos, turn):
    for i in range(len(stairs[0])):
        if stairs[0][i] == pos:
            pos = stairs[1][i]
            #print("Pos stairs" + str(pos))
            turn += 1
            print(str(turn) + ".El jugador sube por escalera al cuadro " + str(pos))
            
    return pos, turn;

"""
input: 
snakes: A list to save the snakes that there are going to be in the board
pos: the current position of the player
output:
The new position of the player and it prints the action thas has been done
"""
def checkSnakes(snakes, pos, turn):
    for i in range(len(snakes[0])):
        if snakes[0][i] == pos:
            pos = snakes[1][i]
            #print("Pos snakes" + str(pos))
            turn += 1
            print(str(turn) + ".El jugador desciende al cuadro " + str(pos))
            
    return pos, turn;

"""
input: 
stairs: A list to save the stairs that there are going to be in the board
snakes: A list to save the snakes that there are going to be in the board
pos: the current position of the player
turn: the current turn of the game
output:
The new position of the player and it prints the action thas has been done and the new turn
"""
def check(stairs, snakes, pos, turn):
    pos, turn = checkStairs(stairs, pos, turn)
    pos, turn = checkSnakes(snakes, pos, turn)
    return pos, turn;

"""
input: 
stairs: A list to save the stairs that there are going to be in the board
snakes: A list to save the snakes that there are going to be in the board
output:
It prints the game flow
"""
def play(stairs, snakes):
    turn = 1
    pos = 1 #current position
    while (pos < 25):
        roll = random.randint(1, 6)
        print(str(turn) + ".Dado arroja " + str(roll))
        turn += 1
        pos += roll
        if pos < 25:
            print(str(turn) + ".El jugador avanza al cuadro " + str(pos))
        if pos >= 25:
            print(str(turn) + ".El jugador supera el cuadro 25")
        #verificar
        pos, turn = check(stairs, snakes, pos, turn)
        turn += 1
    print(str(turn) + ".Fin")
    return 0;

"""
input: 
snakes: A list to save the snakes that there are going to be in the board
heads: A list with the positions where there are snake heads
tails: A list with the positions where there are snake tails 
output:
snakes The list with the heads and the tails of the snakes 
! this function is the same for constructing the stairs
"""
def snakesConstruct(heads, tails):
    #INCLUDE a verification that head and tails lenght are the same
    #INCLUDE a verification that heads and tails numbers are not outside the snakes list
    snakes = []
    # the snake head and tail have the same number for a tail
    snakes.append(heads)
    snakes.append(tails)
    return snakes;

"""
input: 
output:
It prints the game flow
"""
def game():
    board = [i + 1 for i in range(25)] #the board of the game (5x5)
    heads = [22, 24, 19, 14]
    tails = [20, 16, 8, 4]
    stairsS = [10, 9, 6, 3]
    stairsE = [12, 18, 17, 11]
    snakes = snakesConstruct(heads, tails)
    stairs = snakesConstruct(stairsS, stairsE)
    play(stairs, snakes)
    
    return 0;

