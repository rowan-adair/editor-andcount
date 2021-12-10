import re

def averageWordLength(text):
    words = re.split('\s+',text)
    wordCount = len(words)
    
    if wordCount == 0:
        return 0

    ch = 0

    for word in words:
        ch = ch + len(word)

    avg = ch / wordCount
    
    return avg