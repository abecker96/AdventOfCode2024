

def parse_file(file, reports):
    for line in file:
        out = line.split()

        int_arr = list(map(int, out))

        reports.append(int_arr)

def main():
    reports = []
    fail_count = 0
    pass_count = 0

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    with open("input.txt") as file:
        parse_file(file, reports)
    
    for report in reports:
        prev_level = -1 # Initialize prev_level to one that the dataset can't produce
        prev_direction = 0  # Cannot be 0 except after a diff == 0 (fail) condition
        failed = False

        # Look through each level in the report
        for level in report:
            # Can't fail on the first one, just setup history
            if(prev_level < 0):
                prev_level = level
            else:
                diff = abs(prev_level - level)
                direction = 0
                if(prev_level - level < 0):
                    direction = -1  # Doesn't matter if these are positive, negative, or a random number
                else:
                    direction = 1   # Just needs to be different from the other direction

                # Failure conditions
                no_change = diff == 0
                too_much_change = diff > 3
                can_check_direction = prev_direction != 0
                direction_changed = direction != prev_direction

                if(no_change or too_much_change or (can_check_direction and direction_changed)):
                    failed = True
                    break

                prev_direction = direction
                prev_level = level
        
        # Finished analyzing report, tally up results
        if(failed == False):
            pass_count += 1
        else:
            fail_count += 1
        
    # Finished analyzing all reports, print results
    print(f"Pass count: {pass_count}, Fail count: {fail_count}")
            
if __name__ == "__main__":
    main()

#correct answer was 287