# black = 1
# white = 2

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def put(x, y, color):
    grid[x][y] = color

def change_turn(curr_turn):
    if curr_turn == 1: return 2
    else: return 1

def Is_over(curr_grid):
    for i in range(3):
        if (curr_grid[i][0] == curr_grid[i][1] == curr_grid[i][2] & curr_grid[i][0] == 1):
            return "black"
        elif (curr_grid[i][0] == curr_grid[i][1] == curr_grid[i][2] & curr_grid[i][0] == 2):
            return "white"
        else:
            return None
        
def play(grid):
    over = False
    turn = 1
    while True:
        print(grid)
        
        if (Is_over(grid) == "black"):
            print("BLACK WIN")
            break
        elif (Is_over(grid) == "white"):
            print("WHITE WIN")
            break
        
        x = input("x: ")
        y = input("y: ")
        
        put(int(x), int(y), turn)
        turn = change_turn(turn)
        
play(grid)
