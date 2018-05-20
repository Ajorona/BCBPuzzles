 
import sys


def readText(FILE):
     # preprocess
    with open(FILE) as file:
        lines = [line.strip() for line in file]
    lineCount = len(lines)
    genome = lines[:(lineCount-1)]
    k = lines[lineCount-1]
    # get pattern
    text = [ nt for oligo in genome for nt in oligo]
    return (text, int(k))


def writePatterns(FILE, frequentPatterns):
    file = open(FILE, "w+")

    line = ''
    lineCount = 0
    for index, pattern in enumerate(frequentPatterns):
        line += '{} '.format(''.join(pattern))
        if (index+1) % 6 == 0:
            file.write(line + '\n')
            lineCount += 1
            line = ''
    file.write(line + '\n')
    file.close()


def matchPattern(text, index, pattern):
    ''' returns True if the pattern matches the given region of text, false otherwise '''
    ntCount = len(pattern)
    for offset in range(ntCount):
        if text[index+offset] != pattern[offset]:
            return False
    return True

def patternCount(textAndPattern):
    ''' subroutine counts # of pattern occurrences for frequentWords algorithm '''
    count = 0
    text, pattern = textAndPattern
    textLen = len(text)
    patternLen = len(pattern)
    for index in range( (textLen - patternLen) ):
        if matchPattern(text, index, pattern):
            count += 1
    return count


def frequentWords(textAndk):
    text, k = textAndk
    frequentPatterns  = []
    kmerCount = len(text)-k
    count = [patternCount( (text, text[i:(i+k)]) ) for i in range(kmerCount+1)]
    maxCount = max(count)
    for i in range(kmerCount):
        if count[i] == maxCount:
            frequentPatterns.append(text[i:(i+k)])
    pattern_set = set(tuple(pattern) for pattern in frequentPatterns)
    return [list(pattern_tuple) for pattern_tuple in pattern_set]

def main():
    fileName = sys.argv[-1]
    readText(fileName)
    writePatterns('output.txt', frequentWords(readText(fileName)))

main()
