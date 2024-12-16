def bridge_repair(input: list[str]):
    """
        Solved line-by-line, each is independant.
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
    
    # Switched from set to list to account for different equations with the same target!
    calibration_res = list()

    for line in input:
        target, values = line.split(':')
        target, values = int(target), [int(v) for v in values.strip().split()]

        # Number of operators
        n = len(values) - 1

        # Creates all stack permutations
        operator_stacks: list[list[str]] = get_operator_stacks(n)

        target_found = False
        for stack in operator_stacks:
            # Optimisation - stops once a valid set is determined!
            if target_found:
                break

            # Reversed creates a seperate copy, hence there is no need to explicitly create a deepcopy :)
            # Reduces computation time by ~ 1/2
            curr, curr_values = 0, list(reversed(values))

            while curr <= target:
                if len(stack) == 0:
                    # Only counts if the stack is empty! Otherwise, additional operations will cause it to
                    # be greater!
                    if curr == target:
                        target_found = True
                        calibration_res.append(target)
                        # print(f"Adding {target}")

                    break

                operator = stack.pop()
                match operator:
                    case '+':
                        curr_values.append(curr_values.pop() + curr_values.pop())
                    case '*':
                        curr_values.append(curr_values.pop() * curr_values.pop())
                    case '||':
                        curr_values.append(int(str(curr_values.pop()) + str(curr_values.pop())))

                curr = curr_values[-1]

    print(sum(calibration_res))

def get_operator_stacks(n):
    if n == 0:
        return [[]]

    operators = ['+', '*', '||']
    
    return [stack + [operator] for stack in get_operator_stacks(n - 1) for operator in operators]
        
if __name__ == "__main__":
    with open("input.txt", 'r') as input:
        bridge_repair(input.readlines())