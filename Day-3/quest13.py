dic = {'a': "Grl", 'd': "Movie", 'u': "Union", 'T': "Town", 'Q': "Honey", 'R': "rabbit", 's': "Elephant"}
char_array = ['a', 'r', 'T', 's']
for k, v in dic.items():
    if k in char_array:
        print(v)
