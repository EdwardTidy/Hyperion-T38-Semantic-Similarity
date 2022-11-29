import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""I found the similarity between monkey and cat the most interesting as it shows a similarity is there, and more so than just being two animals, which I assume would be just over 0.5. Could it be because they have four limbs? Or fur? Who knows, that's really cool.
"""

print("--------")

# My example is to replace cat with pineapple

tokens2 = nlp('pineapple apple monkey banana')

for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

""" What I found really cool in this case was that pineapple and banana had more similarity than pineapple and apple. Even though apple and pineapple have high similarity (presumably because fruit and the words are similr) banana and pineapple are higher (I'm guessing because they're both yellow and fruit?)
"""

"""Running the file with en_core_web_sm gives a UserWarning: W007 which says the model has no word vectors loaded so instead will be based on tagger, parser and NER. This is evident in the similarity results, for example cat and apple on web_md has a similarity of 0.203... while on web_sm it has a similarity of 0.636... because it is calculating similarity in a different way
"""

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car", "I\'d like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)