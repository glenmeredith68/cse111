import random
import itertools


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
        words = ['a', 'one', 'the', 'this', 'that', 'that-there']
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


def get_adverb():
    '''get adverb'''
    words = [
        'greedily', 'righteously', 'cooly', 'swiftly', 'easily', 'solemnly',
        'proudly', 'wildly', 'cheaply'
    ]
    word = random.choice(words)
    return word


def get_adjective():
    '''get adjective'''
    words = [
        'Abandoned', 'Adventurous', 'Adversarial', 'Advisable', 'Advisory',
        'Aerial', 'Aestival', 'Aetiologic', 'Affable', 'Affected',
        'Affectionate', 'Affective', 'Afferent', 'Affiliated', 'Affirmative',
        'Affordable', 'Afraid', 'African', 'After', 'Aftermost',
        'Aftershafted', 'Agamic', 'Ageless', 'Aggravated', 'Aggravating',
        'Aggressive', 'Aging', 'Agitated', 'Agitative', 'Agleam', 'Aglitter',
        'Aglow', 'Agnate', 'Agnatic', 'Agonizing', 'Agrarian', 'Agreeable',
        'Agreed', 'Agrestic', 'Agricultural', 'Ahead', 'Ahistorical', 'Ahorse',
        'Ailing', 'Aimless', 'Ain', 'Airborne', 'Airheaded', 'Airless',
        'Airlike', 'Airline', 'Airsick', 'Airtight', 'Airworthy', 'Airy',
        'Ajar', 'Alarmed', 'Alarming', 'Alert', 'Algebraic', 'Alien',
        'Alienable', 'Alienated', 'Aliform', 'Alight', 'Aligned', 'Aligning',
        'Alike', 'Alimental', 'Alimentary', 'Alimentative', 'Aliphatic',
        'Aliquot', 'Alive', 'Alkahestic', 'Alkalescent', 'Alkalic', 'Alkaline',
        'All-Around', 'Alleged', 'Allelic', 'Allelomorphic', 'Allergenic',
        'Allergic', 'Alleviatory', 'Alliaceous', 'Allied', 'Alligatored',
        'Allocable', 'Allotted', 'Allover', 'Allowable', 'Alloyed',
        'All-Purpose', 'All-Too-Common', 'Alluring', 'Allusive', 'Alone',
        'Aloof', 'Alpha', 'Alphabetic', 'Alphabetical', 'Alphabetised',
        'Alphabetized', 'Alterable', 'Alternating', 'Alternative', 'Amatory',
        'Amazed', 'Amazing', 'Ambient', 'Ambiguous', 'Ambitious', 'Ambivalent',
        'Ambiversive', 'Amblyopic', 'Ambrosial', 'Ambulant', 'Ambulatory',
        'American', 'Americanized', 'Amiable', 'Amicable', 'Amniotic',
        'Amoeban', 'Amoebic', 'Amoeboid', 'Amoebous', 'Amok', 'Amoristic',
        'Amorous', 'Amorphous', 'Amort', 'Amphibian', 'Ample', 'Amused',
        'Amusing', 'Analgesic', 'Analgetic', 'Analog', 'Analogous', 'Analogue',
        'Babelike', 'Baboonish', 'Babylonian', 'Baccate', 'Bacchanal',
        'Bacchanalian', 'Bacchantic', 'Bacchic', 'Bacciferous', 'Baccivorous',
        'Bacillar', 'Bacillary', 'Bacilliform', 'Back', 'Backbreaking',
        'Backed', 'Backhand', 'Backhanded', 'Backless', 'Backmost',
        'Backstage', 'Backstair', 'Backstairs', 'Backswept', 'Backward',
        'Bacteremic', 'Bactericidal', 'Bacterioid', 'Bacterioidal',
        'Bacteriologic', 'Bacteriological', 'Bacteriolytic', 'Bacteriophagic',
        'Bacteriophagous', 'Bacteriostatic', 'Bacteroid', 'Bacteroidal',
        'Baculiform', 'Bad', 'Baggy', 'Bahai', 'Bahamian', 'Bahraini',
        'Bailable', 'Baked', 'Balanced', 'Balconied', 'Bald', 'Balding',
        'Baleful', 'Balky', 'Ballistic', 'Bally', 'Balmy', 'Baltic',
        'Balzacian', 'Banal', 'Banausic', 'Bandy', 'Baneful', 'Bangladeshi',
        'Bankable', 'Bankrupt', 'Banned', 'Banner', 'Bantam', 'Bantering',
        'Bantoid', 'Bantu', 'Baptised', 'Baptismal', 'Baptistic', 'Baptized',
        'Barbadian', 'Barbarian', 'Barbaric', 'Barbarous', 'Barbate',
        'Barbellate', 'Bare', 'Bareback', 'Barebacked', 'Bared', 'Barefaced',
        'Barefoot', 'Barefooted', 'Barehanded', 'Bareheaded', 'Barelegged',
        'Boric', 'Boring', 'Born', 'Boronic', 'Boskopoid', 'Bosky', 'Bosnian',
        'Bosomed', 'Boss', 'Bossy', 'Botanic', 'Botanical', 'Botchy', 'Both',
        'Different', 'Black', 'Long', 'Little', 'Important', 'Political',
        'Bad', 'White', 'Real', 'Best', 'Right', 'Social', 'Only', 'Public',
        'Sure', 'Low', 'Early', 'Able', 'Human', 'Local', 'Late', 'Hard',
        'Major', 'Better', 'Economic', 'Strong', 'Possible', 'Whole', 'Free',
        'Military', 'True', 'Federal', 'International', 'Full', 'Special',
        'Easy', 'Clear', 'Recent', 'Certain', 'Personal', 'Open', 'Red',
        'Difficult', 'Available', 'Likely', 'Short', 'Single', 'Medical',
        'Current', 'Wrong', 'Private', 'Past', 'Foreign', 'Fine', 'Common',
        'Poor', 'Natural', 'Significant', 'Similar', 'Hot', 'Dead', 'Central',
        'Happy', 'Serious', 'Ready', 'Simple', 'Left', 'Physical', 'General',
        'Environmental', 'Financial', 'Blue', 'Democratic', 'Dark', 'Various',
        'Entire', 'Close', 'Legal', 'Religious', 'Cold', 'Final', 'Main',
        'Green', 'Nice', 'Huge', 'Popular', 'Traditional', 'Cultural'
    ]
    word = random.choice(words)
    return word


def get_preposition():
    '''get preposition'''
    words = [
        'about',
        'above',
        'across',
        'after',
        'against',
        'along',
        'among',
        'around',
        'at',
        'before',
        'behind',
        'below',
        'beneath',
        'beside',
        'between',
        'beyond',
        'by',
        'concerning',
        'down',
        'during',
        'except',
        'for',
        'from',
        'in',
        'inside',
        'into',
        'like',
        'near',
        'of',
        'off',
        'on',
        'onto',
        'out',
        'outside',
        'over',
        'past',
        'regarding',
        'since',
        'through',
        'to',
        'toward',
        'under',
        'underneath',
        'until',
        'up',
        'upon',
        'with',
        'within',
        'without',
    ]
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    for l, m in itertools.pairwise(adjective):
        if l == '-':
            m = m.lower()
            break
    phrase = f'{preposition} {determiner} {adjective.lower()} {noun}'
    return phrase


def assemble_sentence(quantity, tense):
    # quantity = random.randint(1, 2)
    # tense = random.randint(1, 3)

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    adjective = get_adjective()
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f'{determiner.capitalize()} {adjective.lower()} {noun} {verb} {adverb} {prepositional_phrase}.'
    return sentence


main()