

def patternMatching(INPUT):
    """ Returns a list of positions where pattern starts in sequence """
    pattern, sequence = INPUT
    sequenceLen = len(sequence)
    patternLen = len(pattern)
    positions = []
    for i in range( (sequenceLen-patternLen) ):
        startIndex = i
        match = True
        for j in range(patternLen):
            if sequence[i+j] != pattern[j]:
                match = False
                break
        if match == True:
            positions.append(i)
    return positions
