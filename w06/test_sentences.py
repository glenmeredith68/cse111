import imp
from sentences import get_determiner, get_noun, get_adverb, get_verb, get_preposition
import pytest

from sentences import get_prepositional_phrase


def test_get_determiner():
    single_determiners = ['a', 'one', 'the', 'this', 'that', 'that there']
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = [
        'two', 'some', 'those', 'these', 'many', 'the', 'a few',
        'fourty and four'
    ]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners


def test_get_noun():
    singular_nouns = [
        'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'rabbit',
        'woman', 'school'
    ]
    for _ in range(4):
        word = get_noun(1)
        assert word in singular_nouns

    plural_nouns = [
        'birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'men', 'rabbits',
        'women', 'schools'
    ]

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns


def test_get_verb():
    singular_past_verbs = [
        "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked",
        "walked", "wrote"
    ]
    for _ in range(4):
        word = get_verb(range(2), 1)
        assert word in singular_past_verbs

    plural_present_verbs = [
        "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk",
        "walk", "write"
    ]
    for _ in range(4):
        word = get_verb(2, 2)
        assert word in plural_present_verbs

    singular_present_verbs = [
        "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps",
        "talks", "walks", "writes"
    ]
    for _ in range(4):
        word = get_verb(1, 2)
        assert word in singular_present_verbs

    future_verbs = [
        "will drink", "will eat", "will grow", "will laugh", "will think",
        "will run", "will sleep", "will talk", "will walk", "will write"
    ]
    for _ in range(4):
        word = get_verb(range(2), 3)
        assert word in future_verbs


def test_get_preposition():
    prepositions = [
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
    for _ in range(4):
        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrases():
    for _ in range(4):
        phrase = get_prepositional_phrase(1)
        words = phrase.split()
        assert words[1] in ['a', 'one', 'the', 'this', 'that', 'that there']
        assert words[0] in [
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
        assert words[2].capitalize() in [
            'Abandoned', 'Adventurous', 'Adversarial', 'Advisable', 'Advisory',
            'Aerial', 'Aestival', 'Aetiologic', 'Affable', 'Affected',
            'Affectionate', 'Affective', 'Afferent', 'Affiliated',
            'Affirmative', 'Affordable', 'Afraid', 'African', 'After',
            'Aftermost', 'Aftershafted', 'Agamic', 'Ageless', 'Aggravated',
            'Aggravating', 'Aggressive', 'Aging', 'Agitated', 'Agitative',
            'Agleam', 'Aglitter', 'Aglow', 'Agnate', 'Agnatic', 'Agonizing',
            'Agrarian', 'Agreeable', 'Agreed', 'Agrestic', 'Agricultural',
            'Ahead', 'Ahistorical', 'Ahorse', 'Ailing', 'Aimless', 'Ain',
            'Airborne', 'Airheaded', 'Airless', 'Airlike', 'Airline',
            'Airsick', 'Airtight', 'Airworthy', 'Airy', 'Ajar', 'Alarmed',
            'Alarming', 'Alert', 'Algebraic', 'Alien', 'Alienable',
            'Alienated', 'Aliform', 'Alight', 'Aligned', 'Aligning', 'Alike',
            'Alimental', 'Alimentary', 'Alimentative', 'Aliphatic', 'Aliquot',
            'Alive', 'Alkahestic', 'Alkalescent', 'Alkalic', 'Alkaline',
            'All-Around', 'Alleged', 'Allelic', 'Allelomorphic', 'Allergenic',
            'Allergic', 'Alleviatory', 'Alliaceous', 'Allied', 'Alligatored',
            'Allocable', 'Allotted', 'Allover', 'Allowable', 'Alloyed',
            'All-Purpose', 'All-Too-Common', 'Alluring', 'Allusive', 'Alone',
            'Aloof', 'Alpha', 'Alphabetic', 'Alphabetical', 'Alphabetised',
            'Alphabetized', 'Alterable', 'Alternating', 'Alternative',
            'Amatory', 'Amazed', 'Amazing', 'Ambient', 'Ambiguous',
            'Ambitious', 'Ambivalent', 'Ambiversive', 'Amblyopic', 'Ambrosial',
            'Ambulant', 'Ambulatory', 'American', 'Americanized', 'Amiable',
            'Amicable', 'Amniotic', 'Amoeban', 'Amoebic', 'Amoeboid',
            'Amoebous', 'Amok', 'Amoristic', 'Amorous', 'Amorphous', 'Amort',
            'Amphibian', 'Ample', 'Amused', 'Amusing', 'Analgesic',
            'Analgetic', 'Analog', 'Analogous', 'Analogue', 'Babelike',
            'Baboonish', 'Babylonian', 'Baccate', 'Bacchanal', 'Bacchanalian',
            'Bacchantic', 'Bacchic', 'Bacciferous', 'Baccivorous', 'Bacillar',
            'Bacillary', 'Bacilliform', 'Back', 'Backbreaking', 'Backed',
            'Backhand', 'Backhanded', 'Backless', 'Backmost', 'Backstage',
            'Backstair', 'Backstairs', 'Backswept', 'Backward', 'Bacteremic',
            'Bactericidal', 'Bacterioid', 'Bacterioidal', 'Bacteriologic',
            'Bacteriological', 'Bacteriolytic', 'Bacteriophagic',
            'Bacteriophagous', 'Bacteriostatic', 'Bacteroid', 'Bacteroidal',
            'Baculiform', 'Bad', 'Baggy', 'Bahai', 'Bahamian', 'Bahraini',
            'Bailable', 'Baked', 'Balanced', 'Balconied', 'Bald', 'Balding',
            'Baleful', 'Balky', 'Ballistic', 'Bally', 'Balmy', 'Baltic',
            'Balzacian', 'Banal', 'Banausic', 'Bandy', 'Baneful',
            'Bangladeshi', 'Bankable', 'Bankrupt', 'Banned', 'Banner',
            'Bantam', 'Bantering', 'Bantoid', 'Bantu', 'Baptised', 'Baptismal',
            'Baptistic', 'Baptized', 'Barbadian', 'Barbarian', 'Barbaric',
            'Barbarous', 'Barbate', 'Barbellate', 'Bare', 'Bareback',
            'Barebacked', 'Bared', 'Barefaced', 'Barefoot', 'Barefooted',
            'Barehanded', 'Bareheaded', 'Barelegged', 'Boric', 'Boring',
            'Born', 'Boronic', 'Boskopoid', 'Bosky', 'Bosnian', 'Bosomed',
            'Boss', 'Bossy', 'Botanic', 'Botanical', 'Botchy', 'Both',
            'Different', 'Black', 'Long', 'Little', 'Important', 'Political',
            'Bad', 'White', 'Real', 'Best', 'Right', 'Social', 'Only',
            'Public', 'Sure', 'Low', 'Early', 'Able', 'Human', 'Local', 'Late',
            'Hard', 'Major', 'Better', 'Economic', 'Strong', 'Possible',
            'Whole', 'Free', 'Military', 'True', 'Federal', 'International',
            'Full', 'Special', 'Easy', 'Clear', 'Recent', 'Certain',
            'Personal', 'Open', 'Red', 'Difficult', 'Available', 'Likely',
            'Short', 'Single', 'Medical', 'Current', 'Wrong', 'Private',
            'Past', 'Foreign', 'Fine', 'Common', 'Poor', 'Natural',
            'Significant', 'Similar', 'Hot', 'Dead', 'Central', 'Happy',
            'Serious', 'Ready', 'Simple', 'Left', 'Physical', 'General',
            'Environmental', 'Financial', 'Blue', 'Democratic', 'Dark',
            'Various', 'Entire', 'Close', 'Legal', 'Religious', 'Cold',
            'Final', 'Main', 'Green', 'Nice', 'Huge', 'Popular', 'Traditional',
            'Cultural'
        ]
        assert words[3] in [
            'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man',
            'rabbit', 'woman', 'school', 'birds', 'boys', 'cars', 'cats',
            'children', 'dogs', 'men', 'rabbits', 'women', 'schools'
        ]


pytest.main(["-v", "--tb=line", "-rN", __file__])