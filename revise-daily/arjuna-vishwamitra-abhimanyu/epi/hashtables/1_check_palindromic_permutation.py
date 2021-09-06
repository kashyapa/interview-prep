import collections


def check_palindromic_permutation_possible(str):
    map = collections.defaultdict(int)
    count_odd = 0
    
    for c in str:
        if c in map and map[c] % 2 == 1:
            count_odd -= 1
        else:
            count_odd += 1
        map[c] += 1
    return "yes" if count_odd <= 1 else "no"

if __name__ == "__main__":
    s = "lssal"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = ""
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "lsl"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "lafdsfddsl"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "ll"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "l"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
    s = "laaaaa"
    res = check_palindromic_permutation_possible(s)
    print(s + ":" +res)
