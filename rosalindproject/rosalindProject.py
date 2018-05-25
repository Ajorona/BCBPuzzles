import os
import sys
import argparse

from menu import Menu


from frequentWords import matchPattern, patternCount, frequentWords
from reverseComplement import reverseComplement
from patternMatching import patternMatching

importedAlgorithms = ["frequentwords", "reversecomplement", "patternmatching"]


def validateAlgorithmChoice(parser, algorithm):
    if algorithm.lower() not in validAlgorithms:
        parser.error("Cannot find {}".format(algorithm))
        sys.exit(-1)
    else:
        return algorithm.lower()


def readInputFile(algorithm, fileHandle):
    with fileHandle as file:
        lines = [line.strip() for line in file]
    lineCount = len(lines)
    if algorithm == "frequentwords":
        sequence = lines[:(lineCount-1)]
        k = lines[lineCount-1]
        text = [nt for oligo in sequence for nt in oligo]
        return (text, int(k))
    elif algorithm == "reversecomplement":
        text = [nt for oligo in lines for nt in oligo]
        return text
    elif algorithm == "patternmatching":
        pattern = [nt for nt in lines[0]]
        genome = [nt for oligo in lines[1:lineCount] for nt in oligo]
        return (pattern, genome)



def runAlgorithm(algorithm, INPUT, FILENAME=False):
    outputStr = ""
    if algorithm == "frequentwords":
        frequentPatterns = frequentWords(INPUT)
        for i, pattern in enumerate(frequentPatterns):
            line = ''
            for i, pattern in enumerate(frequentPatterns):
                line += '{} '.format(''.join(pattern))
                if (i+1) % 6 == 0:
                    outputStr += (line + '\n')
            if line != '':
                outputStr += (line + '\n')
    elif algorithm == "reversecomplement":
        INPUT = reverseComplement(INPUT)
        line = ""
        for i in range(len(INPUT)):
            outputStr += INPUT[i]
    elif algorithm == "patternmatching":
        startPoints = patternMatching(INPUT)
        for i in range(len(startPoints)):
            outputStr += str(startPoints[i]) + " "
