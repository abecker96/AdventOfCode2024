import time
import copy

DIR_CLOCKWISE = 0
DIR_COUNTERCLOCKWISE = 1

class vec2:
    """Basic helper vec2 class. Missing most functionality."""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    def __mul__(self, other : int):
        return vec2(self.x * other, self.y * other)
    def __rmul__(self, other : int):
        return self.__mul__(other)
    
    def rotate(self, dir):
        # Only works for 90 degree turns, but maintains int types
        if(dir == DIR_CLOCKWISE):
            return vec2(-self.y, self.x)
        else:
            return vec2(self.y, -self.x)
    
DIRECTION_UP = vec2(0, -1)
DIRECTION_DOWN = vec2(0, 1)
DIRECTION_LEFT = vec2(-1, 0)
DIRECTION_RIGHT = vec2(1, 0)

def in_bounds(pos : vec2, xmax : int, ymax : int):
    return ((pos.x >= 0) and (pos.x < xmax) and
            (pos.y >= 0) and (pos.y < ymax))

def walk(map : list[list], pos : vec2, dir: vec2, step = 0):
    next = pos + dir
    xmax = len(map[0])
    ymax = len(map)

    while in_bounds(next, xmax, ymax):
        # Mark the current space as visited, if it isn't already
        map[pos.y][pos.x] = 'X'
        step += 1

        if map[next.y][next.x] == '#':
            # Hit a barrier
            return map, pos, step
        else:
            pos = next
            next = pos + dir
    
    # Walked off the map
    map[pos.y][pos.x] = 'X'
    return map, next, step

def find_startpos(map : list[list]):
    for j, line in enumerate(map):
        for i, c in enumerate(line):
            if(c == '^'):
                return vec2(i, j)

def predict_movements(map : list[list]):
    pos = startpos = find_startpos(map)
    dir = DIRECTION_UP  # Assume we start looking up

    while(in_bounds(pos, len(map[0]), len(map))):
        map, pos, step = walk(map, pos, dir)
        dir = dir.rotate(DIR_CLOCKWISE)
    return map, startpos

def sum_positions(map : list[list]):
    retval = 0
    for line in map:
        retval += sum(1 for el in line if el == 'X')
    return retval

def find_loops(map : list[list], startpos : vec2):
    max_loop_len = 100000
    loops = 0
    for j, line in enumerate(map):
        print(f"Running line {j} of {len(map)}")
        for i, val in enumerate(line):
            if val == 'X': # Only consider visited positions
                newmap = copy.deepcopy(map)
                newmap[j][i] = '#' # Place a barrier at the position

                steps = 0
                pos = startpos
                dir = DIRECTION_UP  # Assume we start looking up
                while((in_bounds(pos, len(map[0]), len(map))) and (steps < max_loop_len)):
                    newmap, pos, steps = walk(newmap, pos, dir, steps)
                    dir = dir.rotate(DIR_CLOCKWISE)

                if steps >= max_loop_len:
                    loops += 1

    return loops


def print_map(map : list[list]):
    for j, line in enumerate(map):
        print(f"line {j + 1:2d}: ", end='')
        for el in line:
            print(el, end=' ')
        print('')

def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""
    start_time = time.perf_counter()
    count = 0

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    map = []

    with open("input.txt") as file:
        for line in file:
            # Convert the string into a list, it'll be easier to deal with
            map.append(list(line))

    map, startpos = predict_movements(map)
    count = find_loops(map, startpos)
    print(count)

    print(f"Number of loops: {count}")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time:.6f} seconds")

if __name__ == "__main__":
    main()

#correct answer was 1812 in ~74s