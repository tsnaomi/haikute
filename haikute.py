#!/usr/bin/env Python

from grammar import grammar, left, right
from random import choice, sample
from dictionary import Dictionary


class Haiku(object):

    def __init__(self):
        self.stanzas = [5, 7, 5]
        self.count = None
        self.line = None
        self.haiku = []
        self.generate()
        # self.edit()

    def __repr__(self):
        return self.haiku

    def generate(self):
        for line, count in enumerate(self.stanzas):
            self.count, self.line = count, []
            self.traverse(line)
            words = len(self.line)

            kosher = False

            while not kosher:

                try:
                    syllables = self.syllabify(words, count)

                    for pos, syll in zip(self.line, syllables):
                        self.haiku.append(choice(Dictionary[pos + str(syll)]))

                    kosher = True

                except KeyError:
                    continue

                except ValueError:  # TODO
                    self.count, self.line = count, []
                    self.traverse(line)
                    words = len(self.line)

            self.haiku.append('\n')

        self.haiku = ' '.join(self.haiku).replace('\n ', '\n')

    def traverse(self, XP):
        Left = choice(grammar[XP][left])
        Right = choice(grammar[XP][right])

        # if the left branch is non-terminal... there is certainly a right
        # branch
        if isinstance(Left, str) and self.count > 1:
            self.traverse(Left)

        # if the left branch is terminal...
        elif Left and (not Right or self.count > 1):
            self.line.append(XP)
            self.count -= 1

        # if the right branch is non-terminal...
        if isinstance(Right, str):
            self.traverse(Right)

        # if the right branch is terminal...
        elif Right:
            self.line.append(XP)
            self.count -= 1

    # stackoverflow.com/questions/3589214/generate-multiple-random-numbers-to-equal-a-value-in-python
    def syllabify(self, n, total):
        dividers = sorted(sample(xrange(1, total), n - 1))
        return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


if __name__ == '__main__':
    for i in range(100):
        print Haiku(), '\n'
