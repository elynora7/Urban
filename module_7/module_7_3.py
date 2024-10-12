class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            file_words = []
            with open(file_name, encoding='utf-8') as f:
                for line in f:
                    new_line = line.lower()
                    for chr in [',', '.', '=', '!', '?', ';', ':']:
                        new_line = new_line.replace(chr, '')
                    new_line = new_line.replace(' - ', ' ')
                    file_words.extend(new_line.split())
            all_words[file_name] = file_words
        return all_words

    def find(self, word):
        results = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                results[name] = words.index(word.lower()) + 1
        return results

    def count(self, word):
        results = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                results[name] = words.count(word.lower())
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))