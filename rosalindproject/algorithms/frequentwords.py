

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

def frequentWords(sequence, k):
    frequentPatterns  = []
    kmerCount = len(sequence)-k
    count = [patternCount( (sequence, sequence[i:(i+k)]) ) for i in range(kmerCount+1)]
    maxCount = max(count)
    for i in range(kmerCount):
        if count[i] == maxCount:
            frequentPatterns.append(sequence[i:(i+k)])
    pattern_set = set(tuple(pattern) for pattern in frequentPatterns)
    return [list(pattern_tuple) for pattern_tuple in pattern_set]
