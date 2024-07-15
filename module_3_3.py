def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 3, 'строка')
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['string', True, 45.6]
values_dict = {'a': 5, 'b': False, 'c': 'string'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [35, 'string']
print_params(*values_list_2, 42)