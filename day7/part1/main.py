import time
from enum import Enum
import itertools

class operators(Enum):
    addition = 1
    multiplication = 2

    def switch(self):
        if self == operators.addition:
            return operators.multiplication
        elif self == operators.multiplication:
            return operators.addition

def run_operation(a, b, op : operators):
    if op == operators.addition:
        return a + b
    elif op == operators.multiplication:
        return a * b
    else:
        return 0
    
def test_equation(eq):
    test_val = eq.pop(0)
    
    # Generate a table of all possible operations
    possible_ops = list(itertools.product([operators.addition, operators.multiplication], repeat=len(eq)-1))

    for ops in possible_ops:
        total = eq[0]
        for i, op in enumerate(ops):
            total = run_operation(total, eq[i+1], op)

        if total == test_val:
            return test_val
    return 0



def main():
    """Main function
    Takes no arguments. Returns no errors. Unless sysio does something really fucky"""
    start_time = time.perf_counter()
    result = 0
    equations = []

    # This could error out if the file isn't found
    # In that case, there isn't a rest of the program to run anyways
    # So no point trying to catch it
    with open("input.txt") as file:
        for line in file:
            eq = []
            eq = list(int(el) for el in line.replace(":", "").split())
            equations.append(eq)

    for eq in equations:
        result += test_equation(eq)
    print(result)

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time:.6f} seconds")

if __name__ == "__main__":
    main()

#correct answer was 1812 in ~74s