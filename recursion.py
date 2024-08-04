def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string
    if len(s) <= 1:
        return s
    else:
        # Recursive step: reverse the substring excluding the first character,
        # then append the first character to the end
        return reverse_string(s[1:]) + s[0]


print(reverse_string('usman'))
