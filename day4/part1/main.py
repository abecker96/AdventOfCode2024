# Problem statement: search the 2D array of text for any occurrences of the
# string "XMAS". Need to search in 8 directions:
# 1 - left->right             * Cardinals
# 2 - right->left
# 3 - top->bottom
# 4 - bottom->top
# 5 - topleft->bottomright    * Diagonals
# 6 - bottomright->topleft
# 7 - topright->bottomleft
# 8 - bottomleft->topright
#
# It might be useful to simplify this to 4 directions, searching for "SAMX"
# as well as "XMAS" instead of doing right->left, for example

search_string = "XMAS"
rowsize = 0
colsize = 0

class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

def slice_2d_str(pos : vec2, direction : vec2, len, str):
    out = ""
    for it in range(len):
        out += str[pos.y+(it*direction.y)][pos.x+(it*direction.x)]
    return out

def construct_options(pos : vec2, file_content):
    options = []
    search_len = len(search_string)

    ltr_direction = vec2(1, 0)
    rtl_direction = vec2(-1, 0)
    ttb_direction = vec2(0, 1)
    btt_direction = vec2(0, -1)

    ltr_space = pos.x + (search_len-1) < rowsize
    rtl_space = pos.x - (search_len-1) >= 0
    ttb_space = pos.y + (search_len-1) < colsize
    btt_space = pos.y - (search_len-1) >= 0

    # Left to right
    if(ltr_space):
        options.append(slice_2d_str(pos, ltr_direction, search_len, file_content))

    # Right to left
    if(rtl_space):
        options.append(slice_2d_str(pos, rtl_direction, search_len, file_content))

    # Top to bottom
    if(ttb_space):
        options.append(slice_2d_str(pos, ttb_direction, search_len, file_content))
    
    # Bottom to top
    if(btt_space):
        options.append(slice_2d_str(pos, btt_direction, search_len, file_content))

    # Top left to bottom right
    if(ltr_space and ttb_space):
        options.append(slice_2d_str(pos, ltr_direction + ttb_direction, search_len, file_content))

    # Bottom right to top left
    if(rtl_space and btt_space):
        options.append(slice_2d_str(pos, rtl_direction + btt_direction, search_len, file_content))

    # Top right to bottom left
    if(rtl_space and ttb_space):
        options.append(slice_2d_str(pos, rtl_direction + ttb_direction, search_len, file_content))

    # Bottom left to top right
    if(ltr_space and btt_space):
        options.append(slice_2d_str(pos, ltr_direction + btt_direction, search_len, file_content))

    return options

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
            for option in construct_options(vec2(j, i), file_content):
                if(option == search_string):
                    count += 1

    print(count)
    
            
if __name__ == "__main__":
    main()

#correct answer was 2504