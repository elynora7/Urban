def all_variants(text):
    stop = len(text) + 1
    for i in range(1, stop):
        for j in range(stop - i):
            yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i)
