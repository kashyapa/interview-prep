# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")


def search_word(board, word):
    def dfs(i, j, index, word):

        if index == len(word):
            return True

        if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]) or (i, j) in visited:
            return False
        print(i, j, index)
        if board[i][j] != word[index]:
            return False

        visited.add((i, j))

        if dfs(i + 1, j, index + 1, word) or dfs(i - 1, j, index + 1, word) \
            or dfs(i, j + 1, index + 1, word) or dfs(i, j - 1, index + 1, word):
            return True
    #    visited.remove((i, j))
        return False

    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0, word):
                    return True
    return False


if __name__ == "__main__":
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']]
    # print(search_word(board, "oath"))
    # print(search_word(board, "f"))
    # print(search_word(board, "x"))
    print(search_word(board, "iflv"))


