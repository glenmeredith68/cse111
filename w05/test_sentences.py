import imp
from sentences import get_determiner, get_noun, get_adjective, get_verb
import pytest


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


pytest.main(["-v", "--tb=line", "-rN", __file__])