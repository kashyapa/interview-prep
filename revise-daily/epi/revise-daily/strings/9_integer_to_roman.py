
def convert_integer_to_roman(n):
    factors = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    i = 0
    roman = []
    while n > 0:
        if n//values[i] > 0:
            d = n // values[i]
            while d > 0:
                roman.append(factors[i])
                d -= 1
            n = n % values[i]
        i += 1
    s = ''.join(roman)
    return s


if __name__ == '__main__':
    print(convert_integer_to_roman(5432))

