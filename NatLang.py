from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Word

new_text = 'Today is a beautiful day. Tomorrow looks like bad weather'
blob = TextBlob(new_text)
print(blob.sentences)
print(blob.words)
print(blob.tags)
print(blob.noun_phrases)
print(blob.sentiment)
blob = TextBlob(new_text, analyzer= NaiveBayesAnalyzer())
print(blob.sentiment)
for sentence in blob.sentences:
    print(sentence.sentiment)
    print()

txt = Word('cat')
print(txt.pluralize())
txt = Word('goats')
print(txt.singularize())
txt = TextBlob('cat goat sheep mouse').words
print(txt.pluralize())
txt = TextBlob('Tis sentnces contans erors')
print(Word('sentnces').spellcheck())
print(txt.correct())





