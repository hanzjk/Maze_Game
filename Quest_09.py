import queue
import time
import csv
from os import system, name 




filename = "maze3.csv"

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  

def createMaze():
    maze = []

    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            maze.append(row)

    return maze


def displayMaze(maze, path=""):
    for a in range(len(maze)):
        for x, pos in enumerate(maze[a]):
            if pos == "S":
                startCol = x
                startRow = a

            #change '1' in the file to '.' which represents the road
            if maze[a][x] == "1":
                maze[a][x] = "."

    clear()

    for r, row in enumerate(maze):
            for c, col in enumerate(row):
                print(col + " ", end="")
            print()
    time.sleep(1)

    i = startCol
    j = startRow
    pos1 = set()
    finalPath=set()
    pos1.add((j, i))
    clear()
    
    for r, row in enumerate(maze):
            for c, col in enumerate(row):
                if (r, c) in pos1:
                    print("R ", end="")
                else:
                    print(col + " ", end="")
            print()
    print()
    time.sleep(1)


    for move in path:
        clear()
        pos1.clear()
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        
        pos1.add((j, i))
        finalPath.add((j,i))
  
        #display the robot path in each step
        for r, row in enumerate(maze):
            for c, col in enumerate(row):
                if (r, c) in pos1:
                    print("R ", end="")
                else:
                    print(col + " ", end="")
            print()
        
        print()
        time.sleep(1)
    
    time.sleep(1)
    clear()
    print("\n\n\t\tROBOT HAS REACHED THE DESTINATION AND THE PATH IS")
    time.sleep(2)
    clear()

    #display the final path indicating '+' sign
    for r, row in enumerate(maze):
            for c, col in enumerate(row):
                if (r, c) in finalPath and maze[r][c]!="D" :
                    print("+ ", end="")

                else:
                    print(col + " ", end="")
            print()
    print()    

#function to check whether the path is valid(check whether there is a brick/border/road) 
def validPath(maze, moves):
    for a in range(len(maze)):
        for x, pos in enumerate(maze[a]):
            if pos == "S":
                startCol = x
                startRow = a

       
    i = startCol
    j = startRow
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        #if the path exceeds the boundary return False
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False

        #if there is a brick return False
        elif (maze[j][i] == "0"):
            return False

    return True


#function to find the destination
def findEnd(maze, moves):
    for a in range(len(maze)):
        for x, pos in enumerate(maze[a]):
            if pos == "S":
                startCol = x
                startRow = a  

    i = startCol
    j = startRow

    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    #if the destination is found, then print and display the maze and return True and if not return False
    if maze[j][i] == "D":
        displayMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM
a_file = open("maze.txt")

lines = a_file.readlines()
clear()
for line in lines:
    print("\t\t\t\t\t"+line,end="")

input("\t\t\t\t\t\t\t  Press Enter to continue...")

nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()
    
#loop through whole map until the destination is found
while not findEnd(maze, add): 
    add = nums.get() #get the first element of the queue
    for j in ["L", "R", "U", "D"]:
        if not(add == ""):
            #neglect some steps such as when previous step is 'L' and current step is 'R' where there is a valid path to again 'L' from
            # 'R' without a brick.

            if j == "L" and add[-1] == "R":
                continue

            elif j == "R" and add[-1] == "L":
                continue

            elif j == "U" and add[-1] == "D":
                continue

            elif j == "D" and add[-1] == "U":
                continue


        put = add + j

        #check whether the added path is valid and if so add it to the queue
        if validPath(maze, put):
            nums.put(put)