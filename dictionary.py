#!/usr/bin/env Python

try:
    import cpickle as pickle

except ImportError:
    import pickle

from collections import defaultdict
from nltk.corpus import brown, cmudict

FILENAME = 'dictionary.pickle'

try:
    Dictionary = pickle.load(open(FILENAME))

except IOError:
    cmudict = cmudict.dict()

    BROWN_CATEGORIES = [
        'lore',
        'learned',
        'fiction',
        'mystery',
        'science_fiction',
        'adventure',
        'romance',
        'humor',
        ]

    VOWELS = [
        'AA0', 'AA1', 'AA2',
        'AE0', 'AE1', 'AE2',
        'AH0', 'AH1', 'AH2',
        'AO0', 'AO1', 'AO2',
        'AW0', 'AW1', 'AW2',
        'AY0', 'AY1', 'AY2',
        'EH0', 'EH1', 'EH2',
        'ER0', 'ER1', 'ER2',
        'EY0', 'EY1', 'EY2',
        'IH0', 'IH1', 'IH2',
        'IY0', 'IY1', 'IY2',
        'OW0', 'OW1', 'OW2',
        'OY0', 'OY1', 'OY2',
        'UH0', 'UH1', 'UH2',
        'UW0', 'UW1', 'UW2',
        ]

    POS_TAGS = [
        'NN', 'NNS', 'JJ', 'RB', 'IN',
        'VB', 'VBD', 'VBG', 'VBN', 'VBZ',
        ]

    D = ['a', 'the', 'this', 'that', 'each', 'some', 'any', 'no', 'what']

    DS = [
        'the', 'these', 'those', 'all', 'some', 'what', 'no', 'them', 'most',
        'more', 'few',
        ]

    def build_dictionary():
        print 'Constructing dictionary...'

        words = set(brown.tagged_words(categories=BROWN_CATEGORIES))
        words = filter(lambda w: w[1] in POS_TAGS, words)
        words.extend([(word, 'D') for word in D])
        words.extend([(word, 'DS') for word in DS])

        dictionary = defaultdict(list)

        for word, pos in words:

            try:
                pos += str(sum(1 for v in cmudict[word][0] if v in VOWELS))
                dictionary[pos].append(word)

            # ignore any words with unknown transcriptions
            except KeyError:
                continue

        print 'Dictionary complete.'

        return dict(dictionary)

    Dictionary = build_dictionary()

    # # pickle the dictionary to file
    # pickle.dump(
    #     Dictionary,
    #     open(FILENAME, 'wb'),
    #     protocol=pickle.HIGHEST_PROTOCOL,
    #     )
