from collections import Counter, namedtuple

Person = namedtuple('Person', ('age', 'name'))


def partitioning_and_sorting(people):
    age_to_count = Counter((a.age for a in people))
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]

        to_age = people[from_idx].age
        to_idx = age_to_offset[to_age]

        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]


if __name__ == '__main__':

    partitioning_and_sorting([Person(34, "sharat"),Person(51, "das"), Person(53, "appa"), Person(64, "pc"), Person(51, "amma"),
                              Person(34, "mucchi"), Person(32, "fsdf")])
