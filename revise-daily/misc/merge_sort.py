def merge(array):
    def merge_sorted_arrays(l1, l2):
        i, j = 0, 0
        merged = []

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1

        merged.extend(l1[i:])
        merged.extend(l2[j:])

        return merged

    if len(array) == 1:
        return array

    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    return merge_sorted_arrays( merge(left_part),  merge(right_part))


if __name__ == "__main__":
    print(merge([-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]))