s = "clcoding"

count_vowels = lambda s: sum(1 for char in s if char.lower() in "aeiou")

print(count_vowels(s))