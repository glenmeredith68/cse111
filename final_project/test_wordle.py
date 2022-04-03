from tkinter import W
import pytest
from wordle import make_word_list, make_answers_list, pick_answer, take_turn, check_guess, you_win


def test_make_word_list():
    word_list = make_word_list()
    assert 'uplit' in word_list
    assert 'thang' in word_list
    assert 'mules' in word_list
    assert 'herbs' in word_list
    assert "etwee" in word_list
    

def test_make_answers_list():
    answers = make_answers_list()
    assert 'seven' in answers
    assert 'heart' in answers
    assert 'laugh' in answers
    assert 'tiger' in answers
    assert 'candy' in answers

def test_pick_answer():
    list1 = make_answers_list()
    answer, list2 = pick_answer(list1)
    assert answer not in list2


# I guess I can't really test a user input function huh? So I won't test you_win() either
# def test_take_turn():
#     usr_input = take_turn()
#     assert len(usr_input) < 6
#     assert usr_input.isalpha()

def test_check_guess():
    answer = 'laugh'
    guess = 'lords'
    incorrect = []
    remaining = []
    green = []
    yellow = []
    check_guess(guess, answer, incorrect, remaining, green, yellow)
    assert 'o' in incorrect

pytest.main(["-v", "--tb=line", "-rN", __file__])