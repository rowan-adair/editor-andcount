import re

def calculateAnds(text):
    words = re.split('\s+',text)
    wordCount = len(words)
    
    count = 0

    if wordCount == 0:
        return count

    for word in words:
        if word == 'and':
            count = count + 1
    
    return count