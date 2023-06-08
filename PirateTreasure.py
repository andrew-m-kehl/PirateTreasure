"""
Pirate Treasure \_{;..;}_/ 
INITIAL MAP
['S', '-', '-', '#', '-', '#', 'T', '#', '-', '-']
['-', '-', '-', '-', '-', '#', '-', '#', '-', '-']
['-', '#', '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '#', '#', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

BFS
TREASURE FOUND!!
[1, 2, 4, '#', 17, '#', 'T', '#', '-', '-']
[3, 5, 7, 9, 13, '#', 34, '#', '-', '-']
[6, '#', 10, 14, 16, 20, 25, 32, '-', '-']
[8, 11, '#', '#', 21, 26, 33, '-', '-', '-']
[12, 15, 18, 22, 27, '-', '-', '-', '-', '-']
['#', 19, 23, 28, '-', '-', '-', '-', '-', '-']
[31, 24, 29, '-', '-', '-', '-', '-', '-', '-']
['-', 30, '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

DFS
TREASURE FOUND!!
[0, 'X', 'X', '#', 'X', '#', 'T', '#', '-', '-']
[1, 'X', 'X', 'X', 'X', '#', 67, '#', '-', '-']
[2, '#', 'X', 'X', 'X', 'X', 66, 65, 64, 63]
[3, '-', '#', '#', 57, 58, 59, 60, 61, 62]
[4, 5, 'X', 'X', 56, 55, 54, 53, 52, 51]
['#', 6, 43, 44, 45, 46, 47, 48, 49, 50]
['-', 7, 42, 41, 40, 39, 38, 37, 36, 35]
['-', 8, 27, 28, 29, 30, 31, 32, 33, 34]
['-', 9, 26, 25, 24, 23, 22, 21, 20, 19]
['-', 10, 11, 12, 13, 14, 15, 16, 17, 18]
"""

from collections import deque

def solve_puzzle(board,source,destination):
    pirate = 0
    moves = [[source[0],source[1]]]
    visited = [[None for x in range(row)] for y in range(col)]
    prev = [[(None) for _ in range(len(board))] for _ in range(len(board[0]))]
    findTreasureDFS(board,source[0],source[1],pirate,0,moves,visited,prev)
    findTreasureBFS(board,source,destination)


def findTreasureBFS(board,source,destination):
    pirate = 0
    y=source[0]
    x=source[1]
    board[y][x] = pirate
    lenY = len(board[0])
    lenX = len(board)
    visited = [[bool(False) for _ in range(lenY)] for _ in range(lenX)]
    visited[y][x] = True

    prev = [[(None) for _ in range(lenY)] for _ in range(lenX)]
    prev[y][x] = 'S'
    end_found = False

    queue = deque([source])

    while queue:
        y,x = queue.popleft()
        pirate+=1
        board[y][x] = pirate
        printBoard(board)

        if (y == destination[0]) and (x == destination[1]):
            print("TREASURE FOUND!!")
            board[y][x] = 'T'
            printBoard(board)
            print("OMG Yaaay :D}{=======D-----------------------------}|")
            end_found = True
            break

        for dx, dy in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            newY = y + dy
            newX = x + dx
            if (0<=newY<len(board)) and (0<=newX<len(board[0])):

                if board[newY][newX] == 'T':
                    queue.insert(0,(newY,newX))
                    visited[newY][newX] = True
                    prev[newY][newX] = (y,x)
                    break

                elif (board[newY][newX] == '-') and (visited[newY][newX] == False):
                    queue.append((newY,newX))
                    visited[newY][newX] = True
                    prev[newY][newX] = (y,x)
    bestPathBFS(y,x,prev,end_found)

def bestPathBFS(y,x,prev,end_found):
    if end_found == True:
        moves = {(1,0):'D',(0,1):'R',(0,-1):'L',(-1,0):'U',}

        bestpath = [(y,x)]
        direction = []
        while prev[y][x] != 'S':
            prevY = prev[y][x][0]
            prevX = prev[y][x][1]
            bestpath.append((prevY,prevX))
            disY = y - prevY
            disX = x - prevX
            direction.append(moves[(disY,disX)])
            x = prevX
            y = prevY
        bestpath.reverse()
        direction.reverse()
        direction = "".join(direction)
        print (bestpath)
        return bestpath, direction
    else:
        return None

def findTreasureDFS(board,x,y,pirate,i,moves,visited,prev):
    "O()"
    board[y][x] = pirate
    visited[y][x] = (y, x)
    printBoard(board)


    while moves:
        for dy, dx in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            newY = y + dy
            newX = x + dx

            if (0<=newX<len(board))and(0<=newY<len(board[0]))and(board[newY][newX]!='#'):

                if board[newY][newX] == 'T':
                    prev[newY][newX] = (y, x)
                    y = newY
                    x = newX
                    visited[y][x] = [(newY,newX)]
                    print("TREASURE FOUND!!")
                    printBoard(board)
                    print("OMG Yaaay :D}{=======D-----------------------------}|")
                    return True
                
                if (board[newY][newX] == '-'):
                    moves.append([newY, newX,pirate+1])
                    prev[newY][newX] = (y,x)
                    if findTreasureDFS(board, newX, newY, pirate + 1,i,moves,visited,prev) == True:
                        return True

        board[y][x] = 'X'
        while (includes([y,x],visited)[0])==True:
            visited.pop(includes([y,x],visited)[1])
        y,x = moves[len(moves)-2][0], moves[len(moves)-2][1]
        moves.pop(len(moves) - 1)
        printBoard(board)
        #visited[x][y] = None

        if findTreasureDFS(board, x, y, pirate -1, i, moves,visited,prev) == True:
            return True
        else:
            return False

    print("Treasure not found.")
    printBoard(board)

def createBoard(row,col,source,destination):
    board = [['-' for y in range(row)] for x in range(col)]

    #Source/Start
    board[source[0]][source[1]]= 'S'

    #Barriers
    board[0][col//2] = '#'
    board[row//2][0] = '#'
    board[2][1] = '#'
    board[3][2] = '#'
    board[3][3] = '#'
    board[0][3] = '#'
    board[1][5] = '#'
    board[0][7] = '#'
    board[1][7] = '#'

    #Destination
    #board[col-1][row-1] = 'T'
    #board[col-1][0] = 'T'
    #board[0][6] = 'T'
    board[destination[0]][destination[1]]= 'T'
    printBoard(board)
    return board

def printBoard(board):
    _=0
    while _ < len(board):
        print(board[_])
        _+=1
    print('\n')

def includes(a,list):
    k=0
    for i in list:
        if a[0] == i[0] and a[1]==i[1]:
            return True,k
        else:
            k+=1
    return False,k


if __name__ == '__main__':
    #myName = (input('Enter name:'))
    row = 10
    col = 10
    source = (0,0)
    destination = (0,6)
    board = createBoard(row,col,source,destination)
    solve_puzzle(board,source,destination)
