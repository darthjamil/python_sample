from urllib.request import urlopen

def get_lines(url):
    response = urlopen(url)
    lines = []

    for line in response:
        lines.append(line.decode('utf-8'))
    
    return lines

def get_words(lines):
    words = [] 

    for line in lines:
        line_words = line.split()

        for word in line_words:
            words.append(word)
    
    return words

def print_words(words):
    for word in words:
        print(word)

lines = get_lines('http://sixty-north.com/c/t.txt')
words = get_words(lines)

print_words(words)
