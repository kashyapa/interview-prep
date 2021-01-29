# Check is string follows a given pattern
def word_pattern_II(s, p):
    def word_pattern_util(offset_s, offset_p):
        if offset_s == len(s) and offset_p == len(p):
            return True
        elif offset_s == len(s) or offset_p == len(p):
            return False

        char_p = p[offset_p]

        if char_p in mapper:
        	substr = mapper[char_p]
        	if s[offset_s:].startswith()