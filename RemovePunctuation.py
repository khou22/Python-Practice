import string

s = "String. With. Punctuation?" # Sample string
out = s.translate(string.maketrans("",""), string.punctuation)

print out
