from collections import namedtuple

VolumeRange = namedtuple('VolumeRange', ('lower', 'higher'))


def can_measure_with_defective_jugs(jugs, L, H):

    def check_if_possible(min_requirement, maximum_allowed):

        if min_requirement > maximum_allowed or VolumeRange(min_requirement, maximum_allowed) in failed_jugs \
            or (min_requirement < 0 and maximum_allowed < 0): \
            return False

        if any(
            (j.lower >= min_requirement and j.higher <= maximum_allowed) or \
            check_if_possible(min_requirement - j.lower, maximum_allowed - j.higher) for j in jugs):
            return True
        failed_jugs.add(VolumeRange(min_requirement, maximum_allowed))
        return False


    failed_jugs = set()
    return check_if_possible(L, H)


def ambiguousMeasurements(measuringCups, low, high):
    def rec(r_low, r_high):

        if r_low > r_high or VolumeRange(r_low, r_high) in c or (r_low < 0 and r_high < 0):
            return False

        for i in range(len(measuringCups)):
            if (measuringCups[i][0] >= r_low and measuringCups[i][1] <= r_high) or rec(r_low - measuringCups[i][0],
                                                                                       r_high - measuringCups[i][1]):
                return True
        c.add(VolumeRange(r_low, r_high))
        return False

    from collections import namedtuple
    VolumeRange = namedtuple('VolumeRange', ('low', 'high'))
    c = set()
    return rec(low, high)



if __name__ == "__main__":
    print(can_measure_with_defective_jugs([VolumeRange(50, 60), VolumeRange(30, 40)], 180, 220))
