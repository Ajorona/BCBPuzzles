

def frequentWordsDecorator(frequentWords, textTuple):
        lines, numLines = textTuple

        k = lines[numLines-1]
        text = lines[:(numLines-1)]
        sequence = [nt for oligo in text for nt in oligo]

        frequentPatterns = frequentWords((k, sequence))

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
        line = ""
        for i in range(len(INPUT)):
            output += INPUT[i]
        return output

def patternMatchingDecorator(patternMatching, textTuple):
        lines, numLines = textTuple

        pattern = [nt for nt in lines[0]]
        sequence = [nt for oligo in lines[1:numLines] for nt in oligo]
        startPoints = patternMatching((pattern, sequence))
        for i in range(len(startPoints)):
            output += str(startPoints[i]) + " "
        return output
