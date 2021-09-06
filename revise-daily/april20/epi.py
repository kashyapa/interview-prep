def reverse_integer(x):
    rev = 0
    sign = 1
    if x < 0:
        sign = -1
    while x > 0:
        rem = x % 10
        x //= 10
        rev = rev*10 + rem
    return rev if sign == 1 else rev * -1


def is_palindrome(x):
    div = 1
    while x // div >= 10:
        div *= 10

    while x > 10:
        r = x % 10
        l = x // div
        if l != r:
            return False
        x = (x % div)//10
    return True


def has_duplicate(block):
    block = list(filter(lambda x: x != 0, block))
    return len(block) != len(set(block))


def check_sudoku(partial_assignment):
    n = len(partial_assignment)

    for i in range(n):
        for j in range(n):
            print(partial_assignment[i])
            print(list((zip(*partial_assignment)))[j])
            if has_duplicate(partial_assignment[i]) or has_duplicate(list((zip(*partial_assignment)))[j]):
                return False
    import math
    region_size = int(math.sqrt(n))
    for I in range(region_size):
        for J in range(region_size):
            flattened_list = []
            for i in range(region_size * I, region_size *(I+1)):
                for j in range(region_size*J, region_size * (J+1)):
                    flattened_list.extend(partial_assignment[i][j])
            if has_duplicate(flattened_list):
                return False
    return True

# replace each 'a' by two 'd's and remove 'b'
def replace_and_remove(str):

    a_count = 0
    write_index = 0
    for i, c in enumerate(str):
        if c != "b":
            if c == "a":
                a_count += 1
            str[write_index] = c
            write_index += 1
    new_write_index = write_index + a_count
    i = write_index
    while i >= 0:
        if str[i] == "a":
            str[new_write_index-1:new_write_index+1] = "dd"
            new_write_index -= 2
        else:
            str[new_write_index] = str[i]
            new_write_index -= 1
        i -= 1
    return write_index + a_count


def test_palindromicity(s):
    i, j = 0, len(s) -1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while j > i and not s[j].isalnum():
            j -= 1
        if s[i] != s[j]:
            return False
    return True

def look_and_say(n):

    def next_number(s):
        count = 1
        res = []
        prev = s[0]
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != prev:
                res.append(str(count) + prev)
                prev = s[i] if i < len(s) else None
                count = 1
            else:
                count += 1
        print(''.join(res))
        return ''.join(res)

    s = "1"
    for i in range(n):
        s = next_number(s)
    print(s)

map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
}
def convert_roman_to_decimal(s):
    sum = map[s[-1]]
    for i in reversed(range((len(s)-1))):
        if map[s[i]] < map[s[i+1]]:
            sum -= map[s[i]]
        else:
            sum += map[s[i]]
    print(sum)

    sum = map[s[-1]]
    for i in reversed(range(len(s)-1)):
        if s[i] < s[i+1]:
            sum -= map[s[i]]
        else:
            sum += map[s[i]]
    print(sum)

VALUES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 1]
SYMBOLS = ["M", "CM".......]
def integer_to_roman(n)
    i = 0
    div = VALUES[i]
    res = []
    while n:
        d = n // VALUES[i]
        for _ in range(d):
            res.append(SYMBOLS[i])
        i += 1
        n = n - d*VALUES[i]
    return "".join(res)



def compute_valid_ip_addresses(s):
    def is_valid(s):
        return len(s) == 1 or s[0] != "0" and int(s) <= 255
    res = []
    parts = [''] * 4

    for i in range(min(4, len(s))):
        parts[0] = s[:i]
        if is_valid(parts[0]):
            for j in range(min(4, len(s)-i)):
                parts[1] = s[i: i+j]
                if is_valid(parts[1]):
                    for k in range(min(4, len(s) - i - j)):
                        parts[2], parts[3] = s[i+j: i + j+ k], s[i+j+k:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            res.append('.'.join(parts))
    return res

def is_substring(s1, s2):

    for i in range(len(s1) - len(s2) + 1):
        if s1[i] == s2[0]:
            j = i
            while j < len(s1):
                if  s1[i+j] != s2[j]:
                    break
                if j < len(s1) and j - i == len(s2):
                    return i
    return -1



if __name__ == "__main__":
    # print(is_palindrome(323))
    # print(is_palindrome(3323))
    # print(is_palindrome(1323))
    # print(is_palindrome(23323))
    # print(is_palindrome(3))

    # matrix = [[1, 2, 3], [4, 5, 6], [1, 8, 9]]
    # print(check_sudoku(matrix))

    convert_roman_to_decimal("XXLC")