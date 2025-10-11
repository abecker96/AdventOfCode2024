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
    with open("input.txt") as file:

        for line in file:
            # Definitely better to just replace this with a regex search
            # this is a terribly inefficient first pass, doing way more string
            # copying than necessary
            # But it could probably be made to be more efficient
            # than the regex with a little effort

            # while(len(line)):
            #     print(f"Start of loop, line: {line}")
            #     index = line.find(startString)

            #     if(index != -1):
            #         # Found, delete the next part of the string
            #         line = line[index + len(startString):]
            #     else:
            #         break

            #     val1 = parseDigits(line)
            #     if(val1 <= 0):
            #         continue
                    
            #     index = line.find(sep)
            #     if(index <= 0 or index > maxDigits):
            #         continue
                
            #     line = line[index+1:]

            #     val2 = parseDigits(line)
            #     if(val2 <= 0):
            #         continue
                
            #     index = line.find(endString)
            #     if(index <= 0 or index > maxDigits):
            #         continue
                
            #     line = line[index+1:]
            #     print(f"Val1: {val1}, Val2: {val2}")
            #     sum += val1 * val2

            # Match any occurrence of the term "mul(d,d)"
            # Where 'd' is 1-3 decimal digits, s.t. the 
            # first digit is not 0
            regex = re.compile(r'mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)')
            # Find all non-overlapping valid strings in the line
            matches = regex.findall(line)

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