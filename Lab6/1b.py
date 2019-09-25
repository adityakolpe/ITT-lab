import string
a = input("String: ")
exclude = set(string.punctuation)
b = ''.join(ch for ch in a if ch not in exclude)
print(b)
