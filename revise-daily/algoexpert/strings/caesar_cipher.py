def caesarCipherEncryptor(s, k):
    # Write your code here.

    # Write your code here.
    res = []
    for i, c in enumerate(s):
        if ord('a') <= ord(c) <= ord('z'):
            nc = ord(c) + k

        if ord(c) + k > ord('z'):
            nc = nc - 26

        res.append(chr(nc))

    return ''.join(res)


if __name__ == "__main__":
    print(caesarCipherEncryptor("xyz", 2))