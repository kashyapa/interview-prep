import collections
from collections import Counter


def generate_document(s, doc):
    d = collections.Counter(doc)
    
    for i, c in enumerate(s):
        if d[c] > 0:
            d[c] -= 1
        else:
            print(c)
            return False
    return True


if __name__ == "__main__":
    print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
