
class Word:
    # ініціалізація обїекту
    def __init__(self, word_en: str, translate_ru: list):
        self.word_en = word_en
        self.translate_ru = translate_ru

    # Відображення слова
    def __repr__(self) -> str:
        return f"Англійське слово:{self.word_en} -> переклад: {self.translate_ru}\n"

class Dictionary:
    # ініціалізація обїекту
    def __init__(self, *words: Word):
        self.words = list(words)

    # додавання нового слова в словник
    def append_word(self, word: Word):
        self.words.append(word)

    # видалення слова з словника
    def remove_word(self, word: Word):
        self.words.remove(word)

    # пошук слова або його перекладу
    def find_word(self, **options: any) -> [Word]:
        words = []
        s = ""
        for word in self.words:
            for option, value in options.items():
                if option == 'translate_ru':
                    seek_value = list(filter(lambda x: value in x, getattr(word, option)))
                    s = ""
                    for i in seek_value: s += str(i)
                else: s = getattr(word, option)
                if s != value: break
                else: words.append(word)
        return words

    # сортування словника
    def sort_word(self, option: str, reverse: bool = False):
        self.words.sort(key=lambda word: getattr(word, option), reverse=reverse)

# ==============================================================================
# створення бібліотеки з першим словом
home_dict = Dictionary(Word("hello", ["привет", "ghbdtn"]))
# додаємо слова в бібліотеку
home_dict.append_word(Word("hello2", ["привет2", "sdsadad", "kkkkkkk"]))
home_dict.append_word(Word("absolut", ["абсолютный", "абсолютный2", "абсолютный3"]))
#
print("==== всі додані слова з словаря =========\n",home_dict.words)
#
print("==== пошук в словарі англійського слова ======\n", home_dict.find_word(word_en="hello2"))
#
print("==== пошук в словарі по перекладу слова ======\n", home_dict.find_word(translate_ru='ghbdtn'))

#
home_dict.sort_word('word_en', True)
print("==== всі додані слова з словаря =========\n",home_dict.words)

#
del_word = home_dict.find_word(translate_ru="привет2")
#for del_word in word:
home_dict.remove_word(del_word)
print("==== всі додані слова з словаря =========\n",home_dict.words)
