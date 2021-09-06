def house_thief(steals):
    def rec(idx):

        if idx == len(steals):
            return 0

        steal_current = steals[idx] + rec(idx+2)
        skip_current = rec(idx+1)

        return max(skip_current, steal_current)
    return rec(0)

