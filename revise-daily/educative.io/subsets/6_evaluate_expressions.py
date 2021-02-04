# Evaluate Expression (hard) #
# Given an expression containing digits and operations (+, -, *),
# find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

# Input: "1+2*3"
# Output: 7, 9
# Explanation: 1+(2*3) => 7 and (1+2)*3 => 9


def diff_ways_to_evaluate_expression(input):
    result = []
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            if not input[i].isdigit():
                left_tree = diff_ways_to_evaluate_expression(input[:i])
                right_tree = diff_ways_to_evaluate_expression(input[i+1:])

                for part1 in left_tree:
                    for part2 in right_tree:
                        if input[i] == "+":
                            result.append(part1 + part2)
                        elif input[i] == "-":
                            result.append(part1 - part2)
                        elif input[i] == "/":
                            result.append(part1/part2)
                        elif input[i] == "*":
                            result.append(part1 * part2)

    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


if __name__ == "__main__":
    main()
