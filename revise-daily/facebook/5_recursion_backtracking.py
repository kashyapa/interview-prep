
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

def count_inversions(nums):

    def count_inversions(nums, start, end):

        def merged_inversion_count(nums, start, mid, end):
            left = mid
            res = []
            inversion_count = 0
            while start < mid and left < end:
                if nums[start] > nums[left]:
                    inversion_count += mid-start
                    res.append(nums[left])
                    left += 1
                else:
                    res.append(nums[start])
                    start += 1
            nums[start:end] = res + nums[start:mid] + nums[mid:end ]

        mid = (start+end) // 2
        lcount = count_inversions(nums, start, mid)
        rcount = count_inversions(nums, mid+1, end)

        return lcount + rcount + merged_inversion_count(nums, start, mid, end)

    return count_inversions(nums, 0, len(nums)-1)


def convert_tree_from_dll(l, n):

    def convert_to_tree(start, end):
        mid = (start+end) // 2

        left = convert_to_tree(start, mid)
        cur, head[0] = head[0] = head[0].next

        cur.prev = left
        cur.next = convert_to_tree(mid+1, end)

        return cur

    head = [l]
    return convert_to_tree(0, n)

# apple
# microsoft
# qualtrics
# servicenow
# intuit
# doordash
# apple
# microsoft


# facebook
# google