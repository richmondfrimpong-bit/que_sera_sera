import spacy

nlp = spacy.load('english')
document = nlp('In 1994 Tim - Bernes Lee founded the world wide web Consortium(W3C)'
               ' devoted to developing web technology')

for entity in document.ents:
    print(f'{entity.text} : {entity.label_}')
