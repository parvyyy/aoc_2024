import copy

def part_1(input: list[str]):
    # Solved line-by-line, each is independant.
    """
        Within each line,


        Create all permutations of '*' and '+'.

        There is always 1 less operator than the # of values.

        Ideally, want it to be in reversed-Polish notation
        (i.e. * + 3 4 5)

        81 * 40 + 27 =  + * 81 40 27

        As operators are always before, we can create 2 ^ n stacks. Test them all.

        An optimisation -- as both + and * increase the value -- if the current
        computation exceeds the target, continue.

        Multiple configarations don't matter. Continue once a single one is determined.
    """
    calibration_res = set()

    for line in input:
        target, values = line.split(':')
        target, values = int(target), [int(v) for v in values.strip().split()]

        # Number of operators
        n = len(values) - 1

        # Creates all stack permutations
        operator_stacks: list[list[str]] = get_operator_stacks(n)

        
        for stack in operator_stacks:
            # Optimisation - stops once a valid set is determined!
            if target in calibration_res:
                break

            curr, curr_values = 0, list(reversed(copy.deepcopy(values)))

            while curr <= target:
                if len(stack) == 0:
                    # Only counts if the stack is empty! Otherwise, additional operations will cause it to
                    # be greater!
                    if curr == target:
                        calibration_res.add(target)

                    break

                operator = stack.pop()
                match operator:
                    case '+':
                        curr_values.append(curr_values.pop() + curr_values.pop())
                    case '*':
                        curr_values.append(curr_values.pop() * curr_values.pop())

                curr = curr_values[-1]


    print(sum(calibration_res))
def get_operator_stacks(n):
    if n == 1:
        return [['+'], ['*']]
    
    all_stacks: list[list[str]] = []
    operators = ['+', '*']
    for stack in get_operator_stacks(n - 1):
        for operator in operators:
            all_stacks.append(stack + [operator])

    return all_stacks
        
if __name__ == "__main__":
    with open("input.txt", 'r') as input:
        part_1(input.readlines())