chaves = ['nome', 'idade', 'cidade']
valores = ['Alice', 30, 'Florianópolis']

my_dict = {}
for key, value in zip(chaves, valores):
    my_dict[key] = value

print(my_dict)