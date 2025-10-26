
ROTATION_CLOCKWISE = 0
ROTATION_COUNTERCLOCKWISE = 1

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
        if(dir == ROTATION_CLOCKWISE):
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