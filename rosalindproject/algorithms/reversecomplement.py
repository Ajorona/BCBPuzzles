
def reverseComplement(text):
    text.reverse()
    for i in range(len(text)):
        if text[i] == 'A':
            text[i] = 'T'
        elif text[i] == 'T':
            text[i] = 'A'
        elif text[i] == 'G':
            text[i] = 'C'
        else:
            text[i] = 'G'
    return text
