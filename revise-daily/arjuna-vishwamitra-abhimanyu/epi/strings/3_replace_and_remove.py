# replace 'a' by 2 'd' and remove 'b'

def replace_and_remove(str):
    a_count = 0
    l = list(str)
    i = 0
    write_index = 0

    while i < len(l):
        if l[i] == "a":
            a_count += 1
        if l[i] != "b":
            l[write_index] = l[i]
            write_index += 1
        i += 1

    l = l + [""] * a_count
    new_write_index = len(l) - 1
    i = write_index
    while i >= 0:
        if l[i] != "a":
            l[new_write_index] = l[i]
            new_write_index -= 1
        else:
            l[new_write_index-1:new_write_index+1] = ["d", "d"]
            new_write_index -= 1
        i -= 1
