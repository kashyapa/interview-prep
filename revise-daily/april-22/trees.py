# def find_lca(root, n1, n2):
#     if root is None:
#         return None
#
#     left_result = find_lca(root.left, n1, n2)
#
#     if left_result.target_nodes == 2:
#         return left_result.lca
#
#     right_result = find_lca(root.right, n1, n2)
#     if right_result.target_nodes == 2:
#         return right_result.lca

#
# class SuffixTrie:
#     def __init__(self, string):
#         self.root = {}
#         self.endSymbol = "*"
#         self.populateSuffixTrieFrom(string)
#
#     def populateSuffixTrieFrom(self, string):
#         for i in range(len(string)):
#             self.insert_substring_starting_at(i, string)
#
#     def insert_substring_starting_at(self, i, string):
#         # Write your code here.
#         node = self.root
#         for j in range(i, len(string)):
#             if string[j] not in node:
#                 node[string[j]] = {}
#             else:
#                 node = node[string[j]]
#         node[self.endSymbol] = True
#
#
# if __name__ == "__main__":
#     trie = SuffixTrie("Sharat Chandra Doddaghatta Shashidhar")
#     print(trie)

from collections import defaultdict


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""


class FileSystem(object):

    def __init__(self):
        self.root = Node()

    def find(self, path):  # find and return node at path.
        curr = self.root
        if len(path) == 1:
            return self.root
        for word in path.split("/")[1:]:
            curr = curr.child[word]
        return curr

    def ls(self, path):
        curr = self.find(path)
        if curr.content:  # file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.child.keys())

    def mkdir(self, path):
        self.find(path)

    def addContentToFile(self, filePath, content):
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath):
        curr = self.find(filePath)
        return curr.content


if __name__ == "__main__":
    fs = FileSystem()
    # fs.mkdir("/root/schandra2/txt.txt")
    # fs.addContentToFile("/root/schandra2/tst.txt", "hello world")
    # content = fs.readContentFromFile("/root/schandra2/tst.txt")
    # print(content)
    print(fs.ls("/root/schandra2"))
    print(fs.ls("/root/"))