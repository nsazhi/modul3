def calculate_structure_sum(*args):
    global calc
    while args:
        for i in args:
            if isinstance(i, int):
                calc += i
                continue
            if isinstance(i, str):
                calc += len(i)
                continue
            if isinstance(i, dict):
                dict_zip = zip(i.keys(), i.values())
                calculate_structure_sum(*dict_zip)
                continue
            else:
                calculate_structure_sum(*i)
        return calc


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calc = 0
result = calculate_structure_sum(data_structure)
print(result)
