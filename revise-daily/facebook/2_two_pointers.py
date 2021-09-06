from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    for w1, w2 in zip(words, words[1:]):
        i, j = 0, 0
        while i < len(w1) and i < len(w2):
            if w1[i] != w2[i]:
                order_w1 = order.index(w1[i])
                order_w2 = order.index(w2[i])

                if order_w1 > order_w2:
                    return False
            i += 1
        if i < len(w1) and i == len(w2):
            return False

    return True


if __name__ == "__main__":
    print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))