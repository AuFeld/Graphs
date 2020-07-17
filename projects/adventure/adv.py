## Understand ## 
'''
# Tasks
- complete the list of directions in adv.py
- construct your own traversal graph. 
    
    1. start in room '0' which contains exits n/s/w/e. should look like:
    {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
    
    2. move south to find yourself in room 5 which constains exits n/s/e
    
    3. you can now fill some entries in your grpah:
    {0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
     5: {'n': 0, 's': '?', 'e': '?'}}
    
# Hints
- test traversal method with smaller graphs
- start by writing an algo (depth first traversal) that:
    1. picks a random unexplored direction from the player's current room
    2. travels and logs [store] that direction from current room
    3. travels and logs [store] that direction, then LOOPS
- you can find the path to the shortest unexploted room by using a BFS for a 
room with a '?' for an exit
- instead of searching for a target vertex, you are searching for an exit with 
a '?' as the value. if an exit has been explored, you put it in your BFS queue
like normal
- BFS will return the path as a list of room ID's. You will need to convert this
to a list of n/s/e/w directions before you can add it your traversal path.
- Research: Maze Travesal

## MVP ##
- len(traversal_path) <= 2000
'''

## Plan ##
'''
- to summarize, what does the player need to do?
    - travel from point A to point B via possible options/exits, n/s/w/e
    - keep track [store] of where we went via rooms visited
    - be able to back track [store] with our player from rooms already visited

- need to be able to back track [store] when a current room is already visited
    - to back track [store] = opposite direction, eg north & south, east & west
    - how to store pre-determined opposite directions
        - list, dict, tup, or set?
            - unorderdered, keys, and values
                - dict {}

- be able to keep track [store] of rooms visited via...
    - list, dict, tup, or set?
        - check whether a specific element [room] is already contained [visited]
            - set()

- need to keep track [store] the path
    - list, dict, tup, or set?
        - list []

- go through [loop] possible directions
    - for loop for possible exits in the current room
        - need:
            - player traveling direction 
            - player current room

- if visited, turn around to previous [opposite] direction
- otherwise, add room to visited and direction to path
    - use recursion to call function again on this room and be able to add it 
    to path
'''
from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


## Execute ##
''' Begin Traversal Code ''' 

# create a dictionary to use when current room is already visited and to go 
# back to the previous room
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def traverse(room, visited=None):
    # create new set
    if visited is None:
        visited = set()

    # create path list
    path = []
    room = player.current_room

    # go through possible directions
    for direction in room.get_exits():
        player.travel(direction)
        room = player.current_room
        # if visited, turn around to previous/opposite direction
        if room in visited:
            player.travel(opposite[direction])
        # otherwise, add room to visited and direction to path
        else:
            visited.add(room)
            path.append(direction)
            # recursively call function again on this room and add to path
            path += traverse(room, visited)
            player.travel(opposite[direction])
            path.append(opposite[direction])
    
    return path 


traversal_path = traverse(player.current_room)

''' End Traversal Code ''' 


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
