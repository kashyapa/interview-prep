from collections import defaultdict


class FileSystem:

    def __init__(self):
        self.root = {}

    def mkDir(self, file_path):
        sub_dirs = file_path.split("/")
        node = self.root

        for dir in sub_dirs:
            if dir not in node:
                node[dir] = {}
            node = node[dir]
        return

    def ls(self, path):
        node = self.root

        sub_dirs = path.split("/")

        for dir in sub_dirs[:-1]:
            if dir not in node:
                return []
            node = node[dir]

        return node.keys()

    def add_content_to_file(self, file_path, content):

        node = self.root

        dirs = file_path.split("/")

        for sub_dir in dirs[:-1]:

            if sub_dir not in node:
                return "path does not exist"
            node = node[sub_dir]
        node[dirs[-1]] = content

    def read_file_from_path(self, path):
        node = self.root

        dirs = path.split("/")

        for d in dirs[:-1]:
            node = node[d]

        return node[dirs[-1]]


if __name__ == "__main__":

    fs = FileSystem()
    fs.mkDir("/root/schandra2")
    fs.add_content_to_file("/root/schandra2/file.txt", "hello world")
    print(fs.read_file_from_path("/root/schandra2/file.txt"))