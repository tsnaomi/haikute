line1 = 0
line2 = 1
line3 = 2

left = 0        # adjunct
right = 1       # head or complement

D = 'D'         # determiner
DS = 'DS'       # determiner (plural)
N = 'NN'        # noun
NS = 'NNS'      # noun (plural)
Adj = 'JJ'      # adjective
Adv = 'RB'      # adverb
P = 'IN'        # preposition
VB = 'VB'       # verb (present, uninflected)
VBZ = 'VBZ'     # verb (present 3rd person)
VBG = 'VBG'     # verb (present participle)
VBD = 'VBD'     # verb (past)
VBN = 'VBN'     # verb (past participle)

# plural VP
{
    'VPS': {
        left: [None, Adv],
        right: [VB, VBD, VBN, VBG],
    },
    # singular VP
    'VP': {
        left: [None, Adv],
        right: [VBZ, VBD, VBN, VBG],
    },
    VB: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBD: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBN: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBG: {
        left: [True, ],
        right: [None, DS, D, P],
    },
}

# i.e., bastardized syntax
grammar = {
    line1: {
        left: [None, ],
        right: [DS, D, P],
    },
    line2: {
        left: [None, ],
        right: ['TP', 'TPS'],
    },
    line3: {
        left: [None, ],
        right: [DS, D],
    },
    'TP': {
        left: [D, ],
        right: ['VP']
    },
    'TPS': {
        left: [DS, ],
        right: ['VPS']
    },
    DS: {
        left: [None, True],
        right: [NS, ],
    },
    NS: {
        left: [None, Adj],
        right: [True, ],
    },
    D: {
        left: [None, True],
        right: [N, ],
    },
    N: {
        left: [None, Adj],
        right: [True, ],
    },
    Adj: {
        left: [None, Adv, Adj],
        right: [True, ],
    },
    Adv: {
        left: [None, ],
        right: [True, ],
    },
    P: {
        left: [True, ],
        right: [DS, D],
    },
    'VPS': {
        left: [None, Adv],
        right: [VB, VBD, VBN, VBG],
    },
    'VP': {
        left: [None, Adv],
        right: [VBD, VBN, VBG],
    },
    VB: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBD: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBN: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBG: {
        left: [True, ],
        right: [None, DS, D, P],
    },
    VBZ: {
        left: [True, ],
        right: [None, DS, D, P],
    },
}
