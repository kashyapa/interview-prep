def search_next_letter(letters, key):
    l, r = 0, len(letters)-1
    while l <= r:
        m = l + (r-l) // 2
        if key == letters[m]:
            return letters[(m+1) % len(letters)]
        if key < letters[m]:
            r = m - 1
        else:
            l = m + 1
    return letters[l % len(letters)]
