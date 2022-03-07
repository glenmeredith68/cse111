import random
from random_word import RandomWords


def main():
    """This is a program that will generate english sentences and pretend to be able to pass the turing test. """

    for j in range(2):
        quantity = j
        for k in range(3):
            tense = k
            sentence = assemble_sentence(quantity, tense)
            print(sentence)


def get_determiner(quantity):
    '''Function to generate articles in a sentence.'''
    if quantity == 1:
        words = ['a', 'one', 'the', 'this', 'that', 'that there']
    else:
        words = [
            'two', 'some', 'those', 'these', 'many', 'the', 'a few',
            'fourty and four'
        ]
    word = random.choice(words)
    return word


def get_noun(quantity):
    '''get noun '''
    if quantity == 1:
        words = [
            'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man',
            'rabbit', 'woman', 'school'
        ]
    else:
        words = [
            'birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'men',
            'rabbits', 'women', 'schools'
        ]
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    '''get verb'''
    if tense == 1:
        words = [
            "drank", "ate", "grew", "laughed", "thought", "ran", "slept",
            "talked", "walked", "wrote"
        ]
    elif tense == 2 and quantity != 1:
        words = [
            "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk",
            "walk", "write"
        ]
    elif tense == 2 and quantity == 1:
        words = [
            "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps",
            "talks", "walks", "writes"
        ]
    else:
        words = [
            "will drink", "will eat", "will grow", "will laugh", "will think",
            "will run", "will sleep", "will talk", "will walk", "will write"
        ]
    word = random.choice(words)
    return word


def get_adjective():
    '''get adjective'''
    words = [
        'greedily', 'righteously', 'cooly', 'swiftly', 'easily', 'solemnly',
        'proudly', 'wildly', 'cheaply'
    ]
    word = random.choice(words)
    return word


def assemble_sentence(quantity, tense):
    # quantity = random.randint(1, 2)
    # tense = random.randint(1, 3)

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    sentence = f'{determiner.capitalize()} {noun} {verb} {adjective}.'
    return sentence


main()