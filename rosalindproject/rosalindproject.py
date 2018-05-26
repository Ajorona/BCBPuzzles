import os
import sys
import argparse

from utilities import Menu

from algorithms.frequentwords import frequentWords
from algorithms.patternmatching import patternMatching
from algorithms.reversecomplement import reverseComplement

from algorithms.algorithmdecorators import frequentWordsDecorator, patternMatchingDecorator, reverseComplementDecorator


class RosalindProject():
    importedAlgorithms = ["frequentwords", "reversecomplement", "patternmatching"]

    def __init__(self, INPUT=None, OUTPUT=None):
        self.INPUT = INPUT
        self.OUTPUT = OUTPUT

    def run(self):
        menu = Menu(RosalindProject.importedAlgorithms)
        self.algorithmChoice = menu.run()
        self.runAlgorithm()

    def runAlgorithm(self):
        with open(self.INPUT, 'rt') as INPUT:
            lines = [line.strip() for line in file]
            numLines = len(lines)
        INPUT.close()

        output = None
        if self.algorithmChoice == "frequentwords":
            output = frequentWordsDecorator(frequentWords, (lines, numLines))
        elif self.algorithmChoice == "reversecomplement":
            output = patternMatchingDecorator(patternMatching, (lines, numLines))
        elif self.algorithmChoice == "patternmatching":
            output = reverseComplementDecorator(reverseComplement, (lines, numLines))

        with open(self.OUTPUT, 'wt') as OUTPUT:
            if output:
                OUTPUT.write(output)
        OUTPUT.close()
