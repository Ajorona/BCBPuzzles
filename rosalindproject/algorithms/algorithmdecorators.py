

def clumpFindingDecorator(clumpFinding, textTuple):
    lines, numLines = textTuple

    params = lines[-1].split()
    k, L, t = [int(param) for param in params]
    lines = lines[0:-1]
    sequence = [nt for oligo in lines for nt in oligo]

    clumps = clumpFinding(k, L, t, sequence)

    # TODO: output formatting


def frequentWordsDecorator(frequentWords, textTuple):
    lines, numLines = textTuple

    k = int(lines[-1])
    text = lines[0:(numLines-1)]
    sequence = [nt for oligo in text for nt in oligo]

    frequentPatterns = frequentWords(sequence, k)

    output = ''
    for i, pattern in enumerate(frequentPatterns):
        line = ''
        for i, pattern in enumerate(frequentPatterns):
            line += '{} '.format(''.join(pattern))
            if (i+1) % 6 == 0:
                output += (line + '\n')
        if line != '':
            output += (line + '\n')
    return output

def reverseComplementDecorator(reverseComplement, textTuple):
    lines, numLines = textTuple
    text = [nt for oligo in lines for nt in oligo]

    INPUT = reverseComplement(text)

    output = ''
    for i in range(len(INPUT)):
        output += INPUT[i]
    return output

def patternMatchingDecorator(patternMatching, textTuple):
    lines, numLines = textTuple
    pattern = [nt for nt in lines[0]]
    sequence = [nt for oligo in lines[1:numLines] for nt in oligo]

    startPoints = patternMatching((pattern, sequence))

    output = ''
    for i in range(len(startPoints)):
        output += str(startPoints[i]) + " "
    return output
