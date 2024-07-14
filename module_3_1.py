def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    len_string = len(string)
    tuple_ = tuple([len_string, string.upper(), string.lower()])
    calls = count_calls()
    return tuple_

def is_contains(string, list_to_search):
    low_string = string.lower()
    for i in range(len(list_to_search)):
        w = list_to_search[i]
        low_w = w.lower()
        if low_string == low_w:
            is_contains = True
            break
        else:
            is_contains = False
    calls = count_calls()
    return is_contains


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
