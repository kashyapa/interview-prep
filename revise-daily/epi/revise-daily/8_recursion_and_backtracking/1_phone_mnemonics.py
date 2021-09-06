def phone_mnemonics(ph_number):

    def phone_mnemonics_rec(partial_res, index):

        if index == len(ph_number):
            result.append(''.join(partial_res))
            return

        s = mapping[int(ph_number[index])]
        for i in range(len(s)):
            partial_res.append(s[i])
            phone_mnemonics_rec(partial_res, index+1)
            partial_res.pop()

        return

    mapping = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")
    result = []
    phone_mnemonics_rec([], 0)
    return result


if __name__ == '__main__':
    print(phone_mnemonics("8573"))