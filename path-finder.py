#import curses
#from curses import wrapper
#import queue
#import time

#maze = [
 # ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
  #["#", " ", " ", " ", " ", " ", " ", " ", "#"],
  #["#", " ", "#", "#", " ", "#", "#", " ", "#"],
  #["#", " ", "#", " ", " ", " ", "#", " ", "#"],
  #["#", " ", "#", " ", "#", " ", "#", " ", "#"],
  #["#", " ", "#", " ", "#", " ", "#", " ", "#"],
  #["#", " ", "#", " ", "#", " ", "#", "#", "#"],
  #["#", " ", " ", " ", " ", " ", " ", " ", "#"],
  #["#", "#", "#", "#", "#", "#", "#", "X", "#"]
#]

#def print_maze(maze, stdscr, path=[]):
 # BLUE = curses.color_pair(1)
  #RED = curses.color_pair(2)
  
  #for i, row in enumerate(maze):
   # for j, value in enumerate(row):
    #  stdscr.addstr(i, j*2, value, BLUE)

#def main(stdscr):
 # curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
  #curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
  
  
  #stdscr.clear()
  #print_maze(maze, stdscr)
  #stdscr.refresh()
  #stdscr.getch()
              #BFS
graph = {
    '5' : ['3', '7'], 
    '3' : ['2', '4'], 
    '7' : ['8'], 
    '2' : [], 
    '4' : ['8'], 
    '8' : []
}
  
visited = [] #List for visited nodes.
queue = [] #Initialize a queue.

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  
  while queue: #Creating loop to visit each node
    s = queue.pop(0)
    print (s, end = " ")
    
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5') #function calling
    