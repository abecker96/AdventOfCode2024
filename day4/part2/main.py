# Problem statement: search the 2D array of text for any occurrences of the
# string "MAS". Need to search in 4 directions:
# 5 - topleft->bottomright    * Diagonals
# 6 - bottomright->topleft
# 7 - topright->bottomleft
# 8 - bottomleft->topright
#

# Probably would make sense to turn this into a class
# if this word search idea goes any further, or this general
# structure turns out to be useful in later problems
search_string = "MAS"
rowsize = 0
colsize = 0

class vec2:
    """Basic helper vec2 class. Missing most functionality."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

def slice_2d_str(pos : vec2, direction : vec2, len, file_content):
    """slice_2d_str function
    Takes an xy position, a direction, a length, and a 2D array of characters
    Returns the string from file_content of length len, starting from the param
    position, and traversing in the specified direction through the file_content
    2D array of characters"""
    out = ""
    for it in range(len):
        out += file_content[pos.y+(it*direction.y)][pos.x+(it*direction.x)]
    return out

def in_bounds(pos : vec2):
    """in_bounds function
    Takes an xy position
    Returns True if the position is a valid position in the 
    file_content 2D list of characters"""
    if((pos.x < 0) or (pos.x >= rowsize) or
       (pos.y < 0) or (pos.y >= colsize)):
        return False
    return True

def construct_options(pos : vec2, file_content):
    """construct_options function
    Takes an xy position and a 2D list of characters as the search area
    Returns a list of 4 strings, where each string represents the diagonal
    slice of characters of len(search_string) which crosses through the
    initial position
    Example: pos = 1,1, file_content = ABC
                                       DEF
                                       GHI
    This function will return the following list:
    retval = [{AEI}, {GEC}, {IEA}, {CEG}]"""
    options = []
    search_len = len(search_string)

    ltr_direction = vec2(1, 0)
    rtl_direction = vec2(-1, 0)
    ttb_direction = vec2(0, 1)
    btt_direction = vec2(0, -1)

    topleft_pos = pos + rtl_direction + btt_direction
    bottomright_pos = pos + ltr_direction + ttb_direction
    topright_pos = pos + ltr_direction + btt_direction
    bottomleft_pos = pos + rtl_direction + ttb_direction

    # Can construct a slice from the top left to the bottom right
    # Also means the other diagonal has a possible slice
    if(in_bounds(topleft_pos) and in_bounds(bottomright_pos)):
        options.append(slice_2d_str(topleft_pos, ltr_direction + ttb_direction, search_len, file_content))
        options.append(slice_2d_str(bottomleft_pos, ltr_direction + btt_direction, search_len, file_content))
        options.append(slice_2d_str(topright_pos, rtl_direction + ttb_direction, search_len, file_content))
        options.append(slice_2d_str(bottomright_pos, rtl_direction + btt_direction, search_len, file_content))

    return options

def validate_options(options):
    """validate_options function
    Takes a list of strings as an argument
    Returns True if at least two of the options
    match the search string"""
    found = 0
    for option in options:
        if(option == search_string):
            found += 1
        
    if(found >= 2):
        return True
    return False

def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""

    count = 0
    global rowsize
    global colsize

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    file_content = []
    with open("input.txt") as file:
        for line in file:
            file_content.append(line)

    # subtract out the \n at the end
    rowsize = len(file_content[0]) - 1
    colsize = len(file_content)

    for i in range(rowsize):
        for j in range(colsize): # ignore newline
            if(validate_options(construct_options(vec2(j, i), file_content))):
                count += 1

    print(count)
    
            
if __name__ == "__main__":
    main()

#correct answer was 1923