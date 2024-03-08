"""
Pirate Treasure! \_{;,,;}_/

Initial Map. 'S' = Start, 'T' = Finish, '#' = Wall
['S', '-', '-', '-', '-', '-', '-', '#', 'T', '-']
['-', '#', '-', '#', '#', '-', '#', '-', '-', '#']
['-', '-', '-', '-', '-', '-', '#', '-', '-', '-']
['-', '-', '-', '-', '#', '#', '-', '-', '#', '-']
['-', '#', '-', '-', '-', '#', '-', '-', '-', '-']
['-', '-', '#', '-', '-', '-', '-', '-', '#', '-']
['#', '-', '-', '-', '#', '-', '#', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '#', '-']
['-', '-', '-', '-', '#', '-', '-', '-', '-', '-']
['-', '-', '#', '-', '-', '-', '-', '-', '-', '-']

BFS Search
[ '1', '2', '4', '6','10','14','18', '#', 'T', '-']
[ '3', '#', '7', '#', '#','19', '#','73','77', '#']
[ '5', '8','11','15','20','24', '#','65','72','76']
[ '9','12','16','21', '#', '#','52','59', '#','71']
['13', '#','22','25','27', '#','47','51','58','64']
['17','23', '#','28','31','36','41','46', '#','68']
[ '#','26','29','32', '#','42', '#','50','56','62']
['35','30','33','37','43','48','53','57', '#','67']
['40','34','38','44', '#','54','60','63','69','74']
['45','39', '#','49','55','61','66','70','75', '-']


Best Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (4, 7), (3, 7), (2, 7), (2, 8), (1, 8), (0, 8)]
['S', '1', '2', '-', '-', '-', '-', '#', 'T', '-']
['-', '#', '3', '#', '#', '-', '#', '-','17', '#']
['-', '-', '4', '5', '-', '-', '#','15','16', '-']
['-', '-', '-', '6', '#', '#', '-','14', '#', '-']
['-', '#', '-', '7', '8', '#', '-','13', '-', '-']
['-', '-', '#', '-', '9','10','11','12', '#', '-']
['#', '-', '-', '-', '#', '-', '#', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-', '#', '-']
['-', '-', '-', '-', '#', '-', '-', '-', '-', '-']
['-', '-', '#', '-', '-', '-', '-', '-', '-', '-']
"""
from collections import deque
import random
import copy
def solve_puzzle(board,source,destination):
    pirate = 0
    moves = [[source[0],source[1]]]
    visited = [[None for x in range(row)] for y in range(col)]
    prev = [[(None) for _ in range(len(board))] for _ in range(len(board[0]))]
    findTreasureDFS(board,source[0],source[1],pirate,0,moves,visited,prev)

def findTreasureBFS(board,source,destination):
    board2 = copy.deepcopy(board)
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
            #print("OMG Yaaay :D}{=======D-----------------------------}|")
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
    bestPathBFS(y,x,prev,end_found,board2)

def bestPathBFS(y,x,prev,end_found,board2):
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
        printBestPath(bestpath,board2)
        return bestpath, direction
    else:
        return None
def printBestPath(bestpath,board2):
    pirate = 1
    queue = deque(bestpath)
    queue.popleft()
    while queue:
        y,x = queue.popleft()
        board2[y][x] = pirate
        pirate+=1
    board2[y][x] = 'T'
    printBoard(board2)

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

                    end_found = True
                    #print (visited)
                    #bestPathDFS(y, x, prev,visited)
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

def createBoard(row,col,source,destination,barriers):
    board = [['-' for y in range(row)] for x in range(col)]

    #Barriers
    for i in range (0,barriers):
        board[random.randint(0, len(board)-1)][random.randint(0, len(board)-1)] = '#'
    # Source/Start
    board[source[0]][source[1]] = 'S'

    #Destination
    board[destination[0]][destination[1]]= 'T'
    printBoard(board)
    return board

def printBoard2(board):
    _=0
    while _ < len(board):
        print(board[_])
        _+=1
    print('\n')

def printBoard(board):
    print('\n')
    arr2 = []
    for i in board:
        for j in i:
            if type(j) == int:
                arr2.append(str(j))
            else:
                arr2.append(j)
        print (arr2)
        arr2 = []


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
    row = 12
    col = 12
    #y = int(input(print("Enter Source y:")))
    #x = int(input(print("Enter Source x:")))
    #source = (y,x)
    source = (random.randint(0, row-1),random.randint(0, col-1))
    #y = int(input(print("Enter Destination y:")))
    #x = int(input(print("Enter Destination x:")))
    #destination = (y,x)
    destination = (random.randint(0, row-1),random.randint(0, col-1))
    #barriers = int(input(print("Enter Amount of Barriers")))
    barriers = (row*col)//4
    board = createBoard(row,col,source,destination,barriers)

    #solve_puzzle(board,source,destination)
    findTreasureBFS(board,source,destination)
