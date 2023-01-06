class Words:
    emp_count = 0

    def __init__(self, word_en, translate_ru):
        self.word_en = word_en
        self.translate_ru = translate_ru
        Words.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Words.empCount)

    def display_word(self):
        print('Слово: {}. Перевод: {}'.format(self.word_en, self.translate_ru))

b1 = Words("hello","Привет, здраствуй")
b1.display_word()

print(getattr(b1, 'word_en'))
delattr(b1,'word_en')
b1.display_word()