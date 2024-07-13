from time import sleep
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    len_string = len(string)
    tuplle_ = tuple([len_string, string.upper(), string.lower()])
    calls = count_calls()
    print(tuplle_)

def is_contains(string, list_to_search):
    list_to_search = list_to_search.split()
    low_string = string.lower()
    # print(low_string)
    for i in range(len(list_to_search)):
        w = list_to_search[i]
        low_w = w.lower()
        # print(w)
        # print(low_w)
        # print(list_to_search)
        if low_string in low_w:
            is_contains = True
            break
        else:
            is_contains = False
    print(is_contains)
    calls = count_calls()

calls = 0
#print(calls)
while True:
    string = input('Введите текст для инфо: ')
    string_info(string)
    print(calls)
    list_to_search = input('Введите список: ')
    string = input('Введите слово для проверки в списке: ')
    is_contains(string, list_to_search)
    print(calls)