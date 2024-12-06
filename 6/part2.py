# Part 1
import line_profiler
import copy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

endkey = "\t"
invalid_chars = ["<", ">", "^", "v", "#"]

# Methods
def print_with_color(text, color, endk=endkey):
    print(f"{color}{text}{bcolors.ENDC}", end=endk)

def get_local():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def get_remote():
    f = open("/home/musa/aoc/6/input", "r")
    return f.read()

@line_profiler.profile
def make_grid(s):
    g = []

    boundary_y = len(s) - 1
    boundary_x = len(s[0]) - 1

    for i in s:
        mainList = []
        for j in i:
            mainList.append(j)
        
        g.append(mainList)

    return g

def format_grid(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            val = g[i][j]
            if val == "^" or val == "v" or val == "<" or val == ">" or val == "#":
                continue

            left = get_grid_spot(g, j - 1, i, False)
            right = get_grid_spot(g, j + 1, i, False)
            top = get_grid_spot(g, j, i - 1, False)
            bottom = get_grid_spot(g, j, i + 1, False)

            if left != None and right != None and top != None and bottom != None:
                g[i][j] = "+"
            elif left != None and right != None:
                g[i][j] = "-"
            elif top != None and bottom != None:
                g[i][j] = "|"

def print_grid(s):
    for colnum in range(len(s)):
        print_with_color(f"{colnum}", bcolors.HEADER)

    print()

    for i in range(len(s)):
        print_with_color(i, bcolors.HEADER, endk=" ")
        for j in range(len(s[i])):
            val = s[i][j]
            if val == "^" or val == "<" or val == ">" or val == "v":
                print_with_color(val, bcolors.OKGREEN)
            else:
                print(val, end=endkey)
        print("\n")

@line_profiler.profile
def find_value_in_grid(grid, value):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                return (i, j)
    
    return None

@line_profiler.profile
def find_occurences_of_value_in_grid(grid, value):
    occurences = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                occurences += 1
    
    return occurences

@line_profiler.profile
def find_gaurd_in_grid(grid):
    left = find_value_in_grid(grid, "<")
    right = find_value_in_grid(grid, ">")
    top = find_value_in_grid(grid, "^")
    bottom = find_value_in_grid(grid, "v")

    if left and not right and not top and not bottom:
        return ("<", left)
    if right and not left and not top and not bottom:
        return (">", right)
    if top and not left and not right and not bottom:
        return ("^", top)
    if bottom and not left and not right and not top:
        return ("v", bottom)
    
    if not left and not right and not top and not bottom:
        return None

    raise Exception("why are there two gaurds?")

@line_profiler.profile
def rotate_guard_right_90_deg(guard):
    match guard:
        case "<":
            return "^"
        case ">":
            return "v"
        case "^":
            return ">"
        case "v":
            return "<"

@line_profiler.profile
def move_guard_left(guard, grid):
    guard_dir = guard[0]
    if guard_dir != "<": raise Exception("Cannot move left when gaurd is not turned left")

    guard_pos = guard[1]
    gpx = guard_pos[1]
    gpy = guard_pos[0]

    # Guard is leaving, simply mark their disappearance
    if gpx - 1 < 0:
        set_grid_spot(grid, "X", gpx,gpy)
        return None
    # Guard hits roadblock
    elif get_grid_spot(grid, gpx - 1,gpy) == "#":
        set_grid_spot(grid, rotate_guard_right_90_deg(guard[0]), gpx,gpy)
        return (get_grid_spot(grid, gpx, gpy), (gpy, gpx))
    else:
        set_grid_spot(grid, "X", gpx,gpy)
        set_grid_spot(grid, "<", gpx - 1, gpy)
        return ("<", (gpy, gpx - 1))

@line_profiler.profile
def move_guard_right(guard, grid):
    guard_dir = guard[0]
    if guard_dir != ">": raise Exception("Cannot move right when gaurd is not turned right")

    boundary_x = len(grid[0]) - 1
    boundary_y = len(grid) - 1

    guard_pos = guard[1]
    gpx = guard_pos[1]
    gpy = guard_pos[0]

    # Guard is leaving, simply mark their disappearance
    if gpx + 1 > boundary_x:
        set_grid_spot(grid, "X", gpx,gpy)
        return None
    # Guard hits roadblock
    elif get_grid_spot(grid, gpx + 1,gpy) == "#":
        set_grid_spot(grid, rotate_guard_right_90_deg(guard[0]), gpx,gpy)
        return (get_grid_spot(grid, gpx, gpy), (gpy, gpx))
    else:
        set_grid_spot(grid, "X", gpx,gpy)
        set_grid_spot(grid, ">", gpx + 1,gpy)
        return (">", (gpy, gpx + 1))

@line_profiler.profile
def move_guard_up(guard, grid):
    guard_dir = guard[0]
    if guard_dir != "^": raise Exception("Cannot move up when gaurd is not turned up")

    boundary_x = len(grid[0]) - 1
    boundary_y = len(grid) - 1

    guard_pos = guard[1]
    gpx = guard_pos[1]
    gpy = guard_pos[0]

    # Guard is leaving, simply mark their disappearance
    if gpy - 1 < 0:
        set_grid_spot(grid, "X", gpx,gpy)
        return None
    # Guard hits roadblock
    elif get_grid_spot(grid, gpx,gpy - 1) == "#":
        set_grid_spot(grid, rotate_guard_right_90_deg(guard[0]), gpx,gpy) 
        return (get_grid_spot(grid, gpx, gpy), (gpy, gpx))
    else:
        set_grid_spot(grid, "X", gpx,gpy)
        set_grid_spot(grid, "^", gpx,gpy - 1)
        return ("^", (gpy - 1, gpx))

@line_profiler.profile
def move_guard_down(guard, grid):
    guard_dir = guard[0]
    if guard_dir != "v": raise Exception("Cannot move down when gaurd is not turned down")

    boundary_x = len(grid[0]) - 1
    boundary_y = len(grid) - 1

    guard_pos = guard[1]
    gpx = guard_pos[1]
    gpy = guard_pos[0]

    # Guard is leaving, simply mark their disappearance
    if gpy + 1 > boundary_y:
        set_grid_spot(grid, "X", gpx,gpy)
        return None
    # Guard hits roadblock
    elif get_grid_spot(grid, gpx,gpy + 1) == "#":
        set_grid_spot(grid, rotate_guard_right_90_deg(guard[0]),gpx,gpy)
        return (get_grid_spot(grid, gpx, gpy), (gpy, gpx))
    else:
        set_grid_spot(grid, "X",gpx,gpy)
        set_grid_spot(grid, "v", gpx,gpy + 1)
        return ("v", (gpy + 1, gpx))

@line_profiler.profile
def get_grid_spot(grid, x, y, throwException=True):
    boundary_x = len(grid[0]) - 1
    boundary_y = len(grid) - 1

    if x > boundary_x or x < 0: 
        if throwException:
            raise Exception("spot does not exist")
        else: return None
    if y > boundary_y or y < 0:
        if throwException:
            raise Exception("spot does not exist")
        else: return None

    return grid[y][x]

@line_profiler.profile
def set_grid_spot(grid, newvalue, x, y):
    get_grid_spot(grid, x, y)
    grid[y][x] = newvalue

@line_profiler.profile
def traverse_once_in_grid(grid, guard):
    # guard = find_gaurd_in_grid(grid)

    match guard[0]:
        case "<":
            return move_guard_left(guard, grid)
        case ">":
            return move_guard_right(guard, grid)
        case "^":
            return move_guard_up(guard, grid)
        case "v":
            return move_guard_down(guard, grid)


def try_traversing_10000_times(grid):
    # this method adds an obstruction to the grid and then tries to traverse the grid 10000 times
    # if we are still traversion the grid after 10000 times, then we have an infinite loop

    guard = find_gaurd_in_grid(grid)
    for i in range(10000):
        if guard == None:
            return False
        guard = traverse_once_in_grid(grid, guard)
        # print_grid(grid)
    return True


def check_each_grid_cell_for_infinite_loop(grid):
    res_list = []
    for i in range(len(grid)):
        print(f"Traversing cell row {i}")
        for j in range(len(grid[i])):
            if grid[i][j] in invalid_chars:
                continue
            else:
                old_grid = copy.deepcopy(grid)
                old = grid[i][j]
                grid[i][j] = "#"
                makes_it_infinite = try_traversing_10000_times(grid)
                res_list.append((makes_it_infinite, (i, j)))
                grid[i][j] = old
                grid = old_grid
        
    return res_list

# Logic

def main():
    f = get_remote()

    s = f.split("\n")
    del s[-1]

    g = make_grid(s)

    # print_grid(g)
    # formtat_grid(g)

    res = check_each_grid_cell_for_infinite_loop(g)

    valid = 0 
    for i in res:
        if i[0] is True:
            valid  += 1
            # print(i)
            # gg = make_grid(s)
            # ypos = i[1][0]
            # xpos = i[1][1]
            # gg[ypos][xpos] = "O"
            # print_grid(gg)

    print(valid)
    # traverse_num = 0
    # guard = find_gaurd_in_grid(g)
    # while guard != None:
    #     if traverse_num % 100 == 0:
    #         print(f"Traversed {traverse_num} times")
    #     guard = traverse_once_in_grid(g, guard)
    #     traverse_num += 1
    #     print()
    #     print_grid(g)

    # o = find_occurences_of_value_in_grid(g, "X")
    # print(f"Found X {o} times in grid")

main()