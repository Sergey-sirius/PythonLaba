class Words:
    def __init__(self, word_en, translate_ru):
        self.word_en = word_en
        self.translate_ru = translate_ru

    def __repr__(self) -> str:
        return f"{self.word_en}: {self.translate_ru}"

class Dictionary():
    def __init__(self, *words: Words):
        self.words = list(words)

    def append_word(self, *words: Words):
        self.words.append(words)
        #self.words.word_en = words[0]
        #self.words.translate_ru = words[1]

# ===================================================
md = Dictionary('hello','привіт, здарово')
print(md.words)
md.append_word('hello2','aadsasd,asdasdas,')
print(md.words)
