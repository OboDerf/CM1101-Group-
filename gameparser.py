import string

skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', '']

def filter_words(words, skip_words):
    for a in words[::-1]:
        if a in skip_words:
            words.remove(a)
    return words

def remove_punct(text):
    for a in text:
        if a in string.punctuation:
            text = text.replace(a, '')
    return text

def normalise_input(user_input):
    return filter_words((remove_punct(user_input).lower()).split(' '), skip_words)

def normalise_str_input(user_input):
    return remove_punct(user_input).lower().strip(" ")
