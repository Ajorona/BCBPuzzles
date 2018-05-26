import os
import sys
import argparse

from utilities import Menu

from algorithms.frequentwords import frequentWords
from algorithms.patternmatching import patternMatching
from algorithms.reversecomplement import reverseComplement
from algorithms.clumpfinding import clumpFinding

from algorithms.algorithmdecorators import frequentWordsDecorator, patternMatchingDecorator, \
                                           reverseComplementDecorator, clumpFindingDecorator


class RosalindProject():
    importedAlgorithms = ["frequentwords", "reversecomplement", "patternmatching", "clumpfinding"]

    def __init__(self, INPUT=None, OUTPUT=None):
        self.INPUT = INPUT
        self.OUTPUT = OUTPUT

    def run(self):
        menu = Menu(RosalindProject.importedAlgorithms)
        self.algorithmSelection = menu.run()
        self.algorithmChoice = RosalindProject.importedAlgorithms[self.algorithmSelection]
        self.runAlgorithm()

    def runAlgorithm(self):
        with open(self.INPUT, 'rt') as INPUT:
            lines = [line.strip() for line in INPUT]
            numLines = len(lines)
        INPUT.close()

        print("choice: {}".format(self.algorithmChoice))
        output = None
        if self.algorithmChoice == "frequentwords":
            output = frequentWordsDecorator(frequentWords, (lines, numLines))
        elif self.algorithmChoice == "reversecomplement":
            output = patternMatchingDecorator(patternMatching, (lines, numLines))
        elif self.algorithmChoice == "patternmatching":
            output = reverseComplementDecorator(reverseComplement, (lines, numLines))
        elif self.algorithmChoice == "clumpfinding":
            output = clumpFindingDecorator(clumpFinding, (lines, numLines))

        with open(self.OUTPUT, 'wt') as OUTPUT:
            if output:
                OUTPUT.write(output)
        OUTPUT.close()
