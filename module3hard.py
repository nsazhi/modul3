def calculate_structure_sum(*args):
    global calc
    for i in args:
        if isinstance(i, int):
            calc += i
        elif isinstance(i, str):
            calc += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, int):
                    calc += key
                if isinstance(key, str):
                    calc += len(key)
                if isinstance(value, int):
                    calc += value
                if isinstance(value, str):
                    calc += len(value)
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
