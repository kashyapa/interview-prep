import string


def first_non_repeating_character(s):
	char_index = {}
	unique_char = set()
	for i, c in enumerate(s):
		if c in char_index:
			if c in unique_char:
				unique_char.remove(c)
		else:
			char_index[c] = 1
			unique_char.add(c)

	for i, c in enumerate(s):
		if c in unique_char:
			return c

	return -1

if __name__ == "__main__":
	print(first_non_repeating_character("faadabcbbebdf"))