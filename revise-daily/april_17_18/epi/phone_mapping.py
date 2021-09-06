def phone_mapping(phone_number):

    def rec(idx, partial_res):
        if idx == len(phone_number):
            res.append(''.join(partial_res.copy()))
            return
        else:
            letters = MAPPING[int(phone_number[idx])]

            for i in range(len(letters)):
                partial_res.append(letters[i])
                rec(idx+1, partial_res)
                partial_res.pop()
            return

    MAPPING = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    res = []
    rec(0, [])
    print(res)


if __name__ == "__main__":
    phone_mapping("85801")