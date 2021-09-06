def inversion_count(nums):
    
    def count_inversion_between(l, r):

        def merge_and_count_inversions(start, mid, end):
            left, right, inversions = start, mid, 0
            sorted_a = []
            while left < m and right < end:
                if nums[left] > nums[right]:
                    inversions += m-left_count
                    right += 1
                    sorted_a.append(nums[right])
                else:
                    left += 1
                    sorted_a.append(nums[left])
            
            nums[l:r] = sorted_a + nums[left:m] + nums[right:end]
            return inversions

        if r - l <= 1:
            return 0

        m = l + (r-l) // 2
        left_count = count_inversion_between(l, m)
        right_count  = count_inversion_between(m+1, r)
        return left_count + right_count + merge_and_count_inversions(l, m, r)