class Jug:
    def __init__(self, lower, higher):
        self.lower = lower
        self.higher = higher


def defective_jugs(lower_limit, higher_limit, jugs:Jug):
    def rec(lower, higher):
        if (lower > higher) or (lower < 0 and higher < 0):
            return False

        for j in jugs:
            if j.lower > lower and j.higher < higher or rec(lower-j.lower, higher-j.higher):
                return True
        failed_set.add((lower, higher))
        return False
    failed_set = set()
    return rec(lower_limit, higher_limit)
