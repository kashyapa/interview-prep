def word_pattern(s, p):
	mapper = {}
	seen = set()
	for i, c in enumerate(s):
		if c in mapper:
			if mapper[c] != p[i]:
				return False
		elif p[i] in seen:
			return False
		else:
			mapper[c] = p[i]
			seen.add(p[i])
	return True


if __name__ == '__main__':
	print(word_pattern("abcac", "catct"))