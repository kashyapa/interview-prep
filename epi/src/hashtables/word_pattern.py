def word_pattern(s, p):
	mapper = {}
	vals = set()
	for i, c in enumerate(s):
		if c in mapper:
			if mapper[c] != p[i]:
				return False
		elif p[i] in vals:
			return False
		else:
			mapper[c] = p[i]
			vals.add(p[i])
	return True

print(word_pattern("abcac", "catct"))