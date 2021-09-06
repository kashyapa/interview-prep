def evaluate_expressions(input):

    result = []

    if "+" not in input and "-" not in input and "*" not in input \
        and "/" not in input:
        result.append(int(result))
    else:

        for i in range(len(input)):
            if not input[i].isdigit():
                left_tree = evaluate_expressions(input[:i])
                right_tree = evaluate_expressions(input[i+1:])

                for part1 in left_tree:
                    for part2 in right_tree:
                        if input[i] == "+":
                            result.append(part1+part2)
                        elif input[i] == "-":
                            result.append(part1-part2)
                        elif input[i] == "/":
                            result.append(part1 / part2)
                        elif input[i] == "*":
                            result.append(part1 * part2)
    return result
