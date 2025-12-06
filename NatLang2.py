import spacy
from pathlib2 import Path
from textblob import TextBlob
from textblob import Word
import pandas as pd
from textatistic import Textatistic
from spacy import language


romeo = TextBlob(str)
print(romeo.word_counts['Romeo'])
print(romeo.word_counts['Juliet'])
print(romeo.word_counts['thou'])

    text = Textatistic()
    print(text.dict())
#new_word = Word('happy')
#for defini in new_word.definitions:
#    print(defini)

#for synonym in new_word.synsets:
#    print(synonym)

#for word in new_word.synsets:
#    vex = word.lemmas()
#    for lemma in vex:
#        print(lemma.antonyms)