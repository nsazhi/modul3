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


# ВАРИАНТ 1
# def unpack(*args, **kwargs):
#     global calc
#     for i in args:
#         # print(i)
#         if isinstance(i, int):
#             calc += i
#         elif isinstance(i, str):
#             calc += len(i)
#         else:
#             unpack(*i)
#     return calc


# calc = 0
# a = [{(2, 'Urban', ('Urban2', 35))}]
# print(unpack(a))

# ВАРИАНТ 2
# def unpack(*args, **kwargs):
#     global calc
#     for i in range(len(args)):
#         el = args[i]
#         # print(el)
#         if isinstance(el, int):
#             calc += el
#             continue
#         elif isinstance(el, str):
#             calc += len(el)
#             continue
#         else:
#             unpack(*el)
#
#
#     return calc
#
#
# calc = 0
# a = [{(2, 'Urban', ('Urban2', 35))}]
# print(unpack(a))