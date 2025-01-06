def single_root_words(root_word, rw = None, ow = None, same_words = None, *other_words):
    if rw = None:
        rw = root_word.lower
        ow = other_words.lower
        same_words = []
        for i in range(len(other_words)):







result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



