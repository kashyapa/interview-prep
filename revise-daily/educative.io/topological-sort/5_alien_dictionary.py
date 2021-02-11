# There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets. Write a method to find the correct order of the alphabets in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.
#
# Example 1:
#
# Input: Words: ["ba", "bc", "ac", "cab"]
# Output: bac
# Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
# from the given words we can conclude the following ordering among its characters:
#
# 1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
# 2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
#
# From the above two points, we can conclude that the correct character order is: "bac"

from collections import deque

def find_order(words):
    graph = {}
    in_degree = {}

    for word in words:
        for character in word:
            in_degree[character] = 0
            graph[character] = []

    for i in range(0, len(words)-1):
        w1, w2 = words[i], words[i+1]
        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    sources = deque()
    for k, v in in_degree.items():
        if v == 0:
            sources.append(k)
    sorted_order = []

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != len(in_degree):
        return ""

    return ''.join(sorted_order)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


if __name__ == "__main__":
    main()
