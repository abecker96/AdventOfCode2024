
startString = "mul("
endString = ")"
sep = ","
maxDigits = 3

def parseDigits(string):
    intString = ""
    while(string[0].isdigit()):
        intString += string[0]
        string = string[1:]

    if(len(intString) > maxDigits):
        # digits too long
        return -1
    elif(len(intString) == 0):
        # not enough digits
        return -1
    else:
        return int(intString)

def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""

    sum = 0
    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    with open("input.txt") as file:

        for line in file:
            while(len(line)):
                index = line.find(startString)

                if(index != -1):
                    # Found
                    line = line[index + len(startString):]

                val1 = parseDigits(line)
                index = line.find(sep)
                line = line[index+1:]
                val2 = parseDigits(line)

                if(val1 > 0 and val2 > 0 and index != -1 and index <= maxDigits):
                    print(f"Val1: {val1}, Val2: {val2}, Index: {index}")
                
                index = line.find(endString)
                
                if(index != -1 and index <= maxDigits):
                    sum += val1 * val2
                    line = line[index+1:]
                    continue


        print(sum)
    
            
if __name__ == "__main__":
    main()

#correct answer was 354