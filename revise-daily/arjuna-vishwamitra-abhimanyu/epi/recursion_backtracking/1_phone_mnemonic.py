def phone_mnemonic(phone_digits):

    def rec(idx):

        if idx == len(phone_digits):
            res.append(mnemonic.copy())
            return
        chars = mapping[int(phone_digits[idx])]

        for c in chars:
            mnemonic.append(c)
            rec(idx+1)
            mnemonic.pop()
        return

    res = []
    mnemonic = []
    mapping = ["0", "1", "ABC", "DEF", "GHI", "JKL",
               "MNO", "PQRS", "TUV", "WXYZ"]

    rec(0)
    return res
