

def parse_file(file, arr1, arr2):
    for line in file:
        out = line.split()
        
        # This could easily error out if the file is formatted improperly
        # It isn't, though
        arr1.append(int(out[0]))
        arr2.append(int(out[1]))

def main():
    arr1 = []
    arr2 = []
    similarity = 0

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    with open("input.txt") as file:
        parse_file(file, arr1, arr2)
    
    dict = {}   # Make a dictionary to count the number of times an element shows up in the list
    # This should be relatively performant if python uses a hashmap underneath
    for key in arr2:
        if f"{key}" in dict:
            dict[f"{key}"] += 1
        else:
            dict[f"{key}"] = 1

    # It might be faster to do this in two iterations to reduce accesses
    # no reason to bother right now, though
    # for key in arr2:
    #     dict[f"{key}"] = 1  # Create the key
    # for key in arr2:
    #     dict[f"{key}"] += 1 # Increment totals

    # If the key exists, add its similarity to the sum
    for key in arr1:
        if f"{key}" in dict:
            similarity += key * dict[f"{key}"]
        # imaginary else
        #   similarity += key * dict[f"{key}"]
        #   but dict[f"{key}"] is just zero so nothing happens
    
    print(similarity)


if __name__ == "__main__":
    main()

# Correct answer was 22776016