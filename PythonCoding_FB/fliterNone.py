your_list = [1,2,3,4,5,None]

filtered_list = list(filter(lambda x: x is not None, your_list))

print(filtered_list)