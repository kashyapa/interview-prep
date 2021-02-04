# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
class Parentheses:
    def __init__(self, s, l_count, r_count):
        self.str = s
        self.lcount = l_count
        self.rcount = r_count


from collections import deque


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(Parentheses("", 0, 0))

    while queue:
        ps = queue.popleft()

        if ps.lcount == num and ps.rcount == num:
            result.append(ps.str)

        else:
            if ps.lcount < num:
                queue.append(Parentheses(ps.str + "(", ps.lcount + 1, ps.rcount))

            if ps.lcount > ps.rcount:
                queue.append(Parentheses(ps.str + ")", ps.lcount, ps.rcount + 1))

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


if __name__ == "__main__":
    main()
