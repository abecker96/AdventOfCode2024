# Problem statement: 


def update_valid(rule_dict : dict, update : list):
    for i in range(len(update)):
        # If a rule doesn't exist enforcing an ordering
        # for this number, it can't be invalid
        if not(update[i] in rule_dict):
            continue

        # Check each number against all of the numbers after it in the list
        for j in range(len(update) - i - 1):
            # If a rule exists where update[i] must come after another number
            # Check to see if any of those numbers exist in the
            # latter part of the update
            for rule in rule_dict[update[i]]:
                if update[1 + i + j] == rule:
                    # Rule violation, no point checking the rest of the list
                    return False
                
    # No invalid orderings found
    return True

def generate_rule_dict(rules):
    rule_dict = {}
    for i in range(len(rules)):
        key = rules[i][1]
        if(key in rule_dict):
            # Don't make duplicate mappings
            continue
        
        # Generate a list of all numbers that must come
        # before this one in an update
        ruleset = []
        for rule in rules:
            if key == rule[1]:
                ruleset.append(rule[0])
        
        # Save that in the return dict
        rule_dict[key] = ruleset

    return rule_dict
        

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

    rule_dict = generate_rule_dict(rules)

    for update in updates:
        if(update_valid(rule_dict, update)):
            # Add midpoint of a valid update to the total
            count += update[len(update)//2]

    print(count)

if __name__ == "__main__":
    main()

#correct answer was 5329