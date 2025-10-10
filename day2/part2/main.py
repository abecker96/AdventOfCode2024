def sign(val):
    """function(a) -> int
    Returns 1, -1, or 0, depending on the sign of (a)"""
    if(val > 0):
        return 1
    elif(val < 0):
        return -1
    else:
        return 0

def parse_file(file):
    """function(file) -> list[list[ints]]
    Takes a file, splits it, and returns a list of lists containing
    the unwrapped integer values on each line."""
    out = []
    for line in file:
        str_arr = line.split()
        int_arr = list(map(int, str_arr))
        out.append(int_arr)
    return out

def is_safe(report, it, it_max):
    """function(report, it, it_max) -> bool
    Takes a report and an iteration count
    Returns True if it (or a valid sublist) is safe within it_max iterations"""
    prev_level = -1 # Initialize prev_level to one that the dataset can't produce
    prev_direction = 0  # Cannot be 0 except after a diff == 0 (fail) condition

    # Can't search too deep into the tree
    if(it > it_max):
        return False

    # Look through each level in the report
    for level in report:
        # Can't fail on the first one, just setup history
        if(prev_level < 0):
            prev_level = level
        else:
            diff = abs(prev_level - level)
            direction = sign(prev_level - level)

            # Failure conditions
            no_change = diff == 0
            too_much_change = diff > 3
            can_check_direction = prev_direction != 0
            direction_changed = direction != prev_direction

            if(no_change or too_much_change or (can_check_direction and direction_changed)):
                # On failure, check sublists for valid lists if a single element was removed
                for i in range(len(report)):
                    new_report = report.copy()
                    del new_report[i]
                    if(is_safe(new_report, it+1, it_max)):
                        return True
                
                # Made it through all sublists with one missing element
                # without finding a safe subset
                return False

            # Save history data
            prev_direction = direction
            prev_level = level

    return True


def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""
    max_depth = 1
    reports = []
    fail_count = 0
    pass_count = 0

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    with open("input.txt") as file:
        reports = parse_file(file)
    
    for report in reports:
        if(is_safe(report, 0, max_depth)):
            pass_count += 1
        else:
            fail_count += 1
        
    # Finished analyzing all reports, print results
    print(f"Pass count: {pass_count}, Fail count: {fail_count}")
            
if __name__ == "__main__":
    main()

#correct answer was 354