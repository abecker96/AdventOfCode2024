# Problem statement: 


def update_valid(rules, update : list):
    # Check each number in the list
    for i in range(len(update)):
        # Against all of the numbers after it in the list
        for j in range(len(update) - i - 1):
            # If a rule exists where
            for rule in rules:
                # update[i] must come after a number which exists in the
                # latter part of the update
                if update[i] == rule[1] and update[1 + i + j] == rule[0]:
                    # Then that is a rule violation
                    return False
    # No invalid orderings found
    return True


def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""

    count = 0

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    rules = []
    updates = []
    example_rule = "dd|dd\n"

    with open("input.txt") as file:
        for line in file:
            # Rules are always the same length
            if(len(line) == len(example_rule)):
                vals = line.strip().split("|")
                rules.append([int(val) for val in vals])
            # Minimum update length is greater than rule length
            elif(len(line) > len(example_rule)):
                vals = line.strip().split(",")
                updates.append([int(val) for val in vals])

    for update in updates:
        if(update_valid(rules, update)):
            count += update[len(update)//2]

    print(count)

        
if __name__ == "__main__":
    main()

#correct answer was 5329