def phone_mnemonics(nums):

    def rec(idx, mnemonic):

        if idx == len(nums):
            res.append(''.join(mnemonic.copy()))
            return
        str = mapping[int(nums[idx])]
        for c in str:
            mnemonic.append(c)
            rec(idx+1, mnemonic)
            mnemonic.pop()
        return


    res = []
    mapping = ['0', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    rec(0, [])
    return res


print(phone_mnemonics("2345"))