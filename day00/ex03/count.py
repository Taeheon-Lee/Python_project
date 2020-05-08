import string


def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if text is None:
        text = input('What is the text to analyse?\n')

    punc = sum((c in string.punctuation) for c in text)
    lower = sum(c.islower() for c in text)
    upper = sum(c.isupper() for c in text)
    spaces = sum(c.isspace() for c in text)

    print('The text contains', len(text), 'characters:\n\n')
    print('-', upper, 'upper letters\n\n')
    print('-', lower, 'lower letters\n\n')
    print('-', punc, 'punctuation marks\n\n')
    print('-', spaces, 'spaces')
