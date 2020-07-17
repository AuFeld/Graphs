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

''' Begin traversal code '''

graph = Graph()
while len(graph.rooms) < len(room_graph):
    this_room = player.current_room
    if this_room.id not in graph.rooms:
        graph.add_room(this_room)
    # random pick from possible directions
    possible_exits = this_room.get_exits()
    direction = random.choice(possible_exits)
    # pick a room not already in the graph
    while this_room.get_room_in_direction(direction).id in graph.rooms and '?' not in graph.get_neighbors(this_room.get_room_in_direction(direction).id).values():
        direction = random.choice(possible_exits)
    # move in chosen direction
    player.travel(direction)
    new_room = player.current_room
    # add this room if it isn't in graph
    if new_room.id not in graph.rooms:
        graph.add_room(new_room)
    # and add it to the traversal path
    traversal_path.append(direction)
    # ensure this new room is connected with the old room
    if new_room.id not in graph.get_neighbors(this_room.id).values():
        graph.add_hall(this_room, new_room, direction)
    # if no unexplored rooms, we're at and end
    if '?' not in graph.get_neighbors(new_room.id).values() and graph.bfs(new_room.id) is not None:
        # we populate the traversal path
        for room_id in graph.bfs(new_room.id):
            for cardinal in ['n', 's', 'e', 'w']:
                room_dir = player.current_room.get_room_in_direction(
                    cardinal)
                if room_dir and room_dir.id == room_id:
                    traversal_path.append(cardinal)
                    player.travel(cardinal)

''' End traversal code '''

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
