class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding= 'utf-8') as file:
                word = file.read().lower()
                all_words[name] = word.split()
        return all_words

    def find(self, word):
        name = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                name[key] = value.index(word.lower()) + 1
        return name


    def count(self, word):
        count = {}
        for key, value in self.get_all_words().items():
            word_count = value.count(word.lower())
            count[key] = word_count
        return count

file_names = []

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))