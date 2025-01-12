def single_root_words(root_word, *other_words, rw = None, ow = None, same_words = None):
    if rw == None and ow == None and same_words == None:
        rw = []
        ow = []
        rw = str(root_word).lower()
        ow = list(other_words)
        same_words = []
        for i in range(len(other_words)):
            if rw in ow[i].lower():
                same_words.append(ow[i])
            elif ow[i].lower() in rw:
                same_words.append(ow[i])

        return same_words








result1 = single_root_words('Rich', 'ricHiest', 'Orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

