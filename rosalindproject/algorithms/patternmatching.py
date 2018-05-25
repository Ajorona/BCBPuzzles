

def patternMatching(INPUT):
    """ Returns a list of positions where pattern starts in sequence """
    pattern, genome = INPUT
    genomeLen = len(genome)
    patternLen = len(pattern)
    positions = []
    for i in range( (genomeLen-patternLen) ):
        startIndex = i
        match = True
        for j in range(patternLen):
            if genome[i+j] != pattern[j]:
                match = False
                break
        if match == True:
            positions.append(i)
    return positions
