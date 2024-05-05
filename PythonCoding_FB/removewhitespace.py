your_list = [" hello ", "world   ", "    python " ]

#strip functions is used to remove white space
trimmed_stings = list(map(lambda x: x.strip(), your_list))
print(trimmed_stings)