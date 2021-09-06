from collections import deque


class FileSystem:

    def __init__(self):
        self.root = {}


    def ls(self, path: str):
        sub_dirs = path.split("/")

        node = self.root

        for dir in sub_dirs[:-1]:
            if dir not in node:
                return []
            node = node[dir]
        return node.items()

    def mkdir(self, path: str):
        sub_dirs = path.split("/")

        node = self.root

        for dir in sub_dirs:
            if dir not in node:
                node[dir] = {}
            node = node[dir]


    def addContentToFile(self, filePath: str, content: str):
        sub_dirs = filePath.split("/")

        node = self.root

        for dir in sub_dirs[:-1]:
            if dir not in node:
                return []
            node = node[dir]

        file_name = sub_dirs[-1]
        node[file_name] = content


    def readContentFromFile(self, filePath: str):
        sub_dirs = filePath.split("/")

        node = self.root

        for dir in sub_dirs[:-1]:
            if dir not in node:
                return []
            node = node[dir]

        file_name = sub_dirs[-1]
        return node[file_name]


def minimum_knight_moves(x, y):

    visited = set()
    queue = deque([(0, 0, 0)])

    while queue:

        p, q, steps = queue.popleft()
        if (p, q) == (x, y):
            return steps

        visited.add((p, q))
        i, j = p, q
        for p, q in [(i+2, j-1), (i+2, j+1), (i+1, j+2), (i+1, j-1), (i-1, j+2), (i-2, j+1)]:
            queue.append((p, q, steps+1))

    return -1


class TicTacToe:
    def __init__(self, n: int):
        self.row=[0]*n
        self.col=[0]*n
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row] += 1 if player==1 else -1
        self.col[col] += 1 if player==1 else -1
        if row+col==self.n-1:
            self.diag1+=1 if player==1 else -1
        if row-col==0:
            self.diag2+=1 if player==1 else -1
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
            return 1 if player==1 else 2
        return 0


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.hot = 0
        self.children = {}


class Autocomplete:

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.search_term = ""

        for sentence in sentences:
            for i in range(len(sentence)):
                self.add(sentence[:i])

    def add(self, word):
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.is_end = True
        node.hot -= 1

    def dfs(self, res, path, node):

        if node.is_end:
            res.append(path)

        for c in node.children:
            self.dfs(res, path+c, node.children[c])

    def search(self):
        node = self.root
        res = []
        path = []
        for c in self.search_term:
            if c not in node.children:
                return []
            node = node.children[c]
            path += c

        self.dfs(res, path, node)
        return [item[1] for item in sorted(res[:3])]

    def input(self, c):

        if c != "#":
            self.search_term += c
            return self.search()

from collections import Counter

def word_break(big_str, words):
    if not big_str:
        return True

    for w in words:
        substr = big_str[:len(w)]
        return word_break(big_str[len(w):])


    for i in range(len(big_str)):
        j = i
        word_freq = Counter(words)
        while j < len(big_str):



if __name__ == "__main__":
    fs = FileSystem()
    fs.mkdir("/root/schandra2")
    fs.addContentToFile("/root/schandra2/file.txt", "hello world")
    print(fs.readContentFromFile("/root/schandra2/file.txt"))
    print(fs.ls("/root/schandra2"))


