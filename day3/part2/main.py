import re

def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""

    sum = 0
    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    with open("input.txt") as file:
        do_str = "do()"
        dont_str = "don't()"

        # File starts with an enabled section, strip that out first
        enabled = True  # Make sure to remember enabled status between lines
        for line in file:
            do_section = ""

            while(len(line)):
                # There are far more efficient ways to do this than constant string splicing
                # This is fast enough for right now though. If anybody else were to run this
                # on worse hardware, or on larger datasets, this would be a prime section
                # for optimization
                if((line.startswith(do_str) and not enabled) or 
                   (line.startswith(dont_str) and enabled)):
                    enabled = not enabled
                
                if(enabled):
                    do_section += line[:1]
                line = line[1:]
                    
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