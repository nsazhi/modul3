def single_root_words(root_word, *other_words):
    same_words =[]
    # print(other_words)
    for i in other_words:
        low_root = root_word.lower()
        low_other = i.lower()
        if low_root in low_other:
            same_words.append(i)
            continue
        if low_other in low_root:
            same_words.append(i)
            continue
    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')