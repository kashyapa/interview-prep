def substring_search(s1, s2):

    for i in range(len(s1)):
        if s1[i] == s2[0]:
            j = 0
            while j < len(s2) and i +j < len(s1):
                if s1[i+j] != s2[j]:
                    break
                j += 1
            if j == len(s2):
                return i
    return -1

if __name__ == "__main__":
    res = substring_search("Hello", "elo")
    print(res)
