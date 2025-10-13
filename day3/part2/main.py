import re


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
    with open("test_input.txt") as file:
        do_str = "do()"
        dont_str = "don't()"

        for line in file:
            # File starts with an enabled section, strip that out first
            enabled = True
            do_section = ""
            dont_section = ""

            while(len(line)):
                if(enabled):
                    search_str = dont_str
                    index = line.find(dont_str)
                    if(index == -1):
                        break
                    do_section += line[:index]
                    print(f"Do: {do_section}")
                    print(f"Dont: {dont_section}")
                else:
                    search_str = do_str
                    index = line.find(do_str)
                    if(index == -1):
                        break
                    dont_section += line[:index]
                    print(f"Do: {do_section}")
                    print(f"Dont: {dont_section}")

                line = line[index:]
                enabled = not enabled


            
            print(f"Final do: {do_section}")
            # Match any occurrence of the term "mul(d,d)"
            # Where 'd' is 1-3 decimal digits, s.t. the 
            # first digit is not 0
            regex = re.compile(r'mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)')
            # Find all non-overlapping valid strings in the line
            matches = regex.findall(do_section)

            # Get a string containing decimal digits
            # This one can be simpler, the first regex already
            # made sure that the string has a valid number of digits
            digitregex = re.compile(r'\d+')
            
            for match in matches:
                # Get digits out of the string
                digits = digitregex.findall(match)
                # Array accesses are find, we've already validated the string
                sum += int(digits[0]) * int(digits[1])


        print(sum)
    
            
if __name__ == "__main__":
    main()

#correct answer was 173419328