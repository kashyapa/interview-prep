from collections import deque

def find_subsets(nums):
    
    subsets = deque([])
    subsets.append([])
    for i in range(len(nums)):
        
        n = len(subsets)
        
        for j in range(n):
            p = list(subsets[j])
            p.append(nums[i])
            subsets.append(p)
    return subsets


def find_subsets_with_duplicates(nums):

    subsets = []
    subsets.append([])

    start, end = -1, -1

    for i in range(len(nums)):
        start = 0

        if i > 0 and nums[i] == nums[i-1]:
            start = end

        end = len(subsets)
        for j in range(start, end):
            new_set = list(subsets[j])
            new_set.append(nums[i])
            subsets.append(new_set)
    return subsets


def find_permutations(nums):

    perms = deque([])
    perms.append([])
    res = []

    for i in range(len(nums)):

        n = len(perms)

        for j in range(n):
            old_perm = perms.popleft()

            for k in range(len(old_perm)+1):
                new_perm = list(old_perm)
                new_perm.insert(k, nums[i])
                if len(new_perm) == len(nums):
                    res.append(new_perm)
                perms.append(new_perm)

    return res


def find_letter_case_string_permutations(letters):

    perms = deque([letters])

    for i in range(len(letters)):
        if letters[i].isalpha():
            n = len(perms)

            for j in range(n):
                p = perms[j]

                new_p = list(p)
                new_p[i] = new_p[i].swapcase()
                perms.append(''.join(new_p))
    return perms

class Parentheses:
    def __init__(self, lc, rc, p):
        self.lcount = lc
        self.rcount = rc
        self.parentheses = p


def generate_valid_parentheses(n):

    q = deque([])
    q.append(Parentheses(0, 0, ""))
    res = []
    while q:
        p = q.popleft()
        if p.lcount == p.rcount == n:
            res.append(p.parentheses)
        else:
            if p.lcount < n:
                q.append(Parentheses(p.lcount+1, p.rcount, p.parentheses+"("))

            if p.rcount < p.lcount:
                q.append(Parentheses(p.lcount, p.rcount+1, p.parentheses+")"))
    return res


def diff_ways_to_evaluate_expression(input):
    def rec(start, end):
        res = []
        partial_input = input[start:end]
        if "+" not in partial_input and "-" not in partial_input and "*" not in partial_input and "/" not in partial_input:
            res.append(input[start:end])
        else:
            for i in range(start, end):
                if input[i] in ("+", "-", "*", "/"):
                    left_results = rec(start, i)
                    right_results = rec(i+1, end)
                    for part1 in left_results:
                        for part2 in right_results:
                            if input[i] == "+":
                                res.append(int(part1) + int(part2))
                            if input[i] == "-":
                                res.append(int(part1) - int(part2))
                            if input[i] == "*":
                                res.append(int(part2) * int(part1))
                            if input[i] == "/":
                                res.append(int(part1) // int(part2))
        return res

    return rec(0, len(input))

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def find_unique_trees(n):

    def rec(start, end):

        res = []

        if start > end:
            res.append(None)
            return res
        for i in range(start, end+1):

            left_results = rec(start, i-1)
            right_results = rec(i+1, end)

            for lr in left_results:
                for rr in right_results:
                    root = TreeNode(i)
                    root.left = lr
                    root.right = rr
                    res.append(root)
        return res
    
    return rec(0, n)

# def main():
#     print("Here is the list of subsets: " + str(find_subsets([1, 3])))
#     print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
#
# if __name__ == "__main__":
#     main()
def main():
    # print("Here is the list of subsets: " + str(find_subsets_with_duplicates([1, 3, 3])))
    # print("Here is the list of subsets: " + str(find_subsets_with_duplicates([1, 5, 3, 3])))
    # print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    # print("String permutations are: " +
    #       str(find_letter_case_string_permutations("ad52")))
    # print("String permutations are: " +
    #       str(find_letter_case_string_permutations("ab7c")))

    # print("All combinations of balanced parentheses are: " +
    #       str(generate_valid_parentheses(2)))
    # print("All combinations of balanced parentheses are: " +
    #       str(generate_valid_parentheses(3)))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))

if __name__ == "__main__":
    main()
