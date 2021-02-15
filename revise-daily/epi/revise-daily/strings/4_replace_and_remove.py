# replace each 'a' by two 'd's and remove 'b'


def replace_and_remove(str):
    write_index = 0
    a_count = 0

    for i in range(len(str)):
        if str[i] != 'b':
            str[write_index] = str[i]
            write_index += 1
        if str[i] == 'a':
            a_count += 1

    cur_idx = write_index - 1
    write_index += a_count - 1
    final_size = write_index + 1
    while cur_idx >= 0:
        if str[cur_idx] == "a":
            str[write_index - 1: write_index+1] = "dd"
            write_index -= 2
        else:
            str[write_index] = str[cur_idx]
            write_index -= 1
        cur_idx -= 1
    return final_size
