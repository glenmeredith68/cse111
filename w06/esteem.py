def main():
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')
    print('')
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')

    total_score = 0

    total_score = ask_questions(total_score)

    print(f'Your Score on the Assesment was {total_score}')
    if total_score < 15:
        print(
            'You scored below 15, it could indicate problamatic low self-esteem.'
        )
    elif total_score > 15:
        print('You scored above 15, indicates a high form of self-esteem.')


def answer(question, total_score):
    response = input('Enter D, d, a, or A:')

    questions = [1, 2, 4, 6, 7]
    if question in questions:
        if response == 'D':
            score = 0
        elif response == 'd':
            score = 1
        elif response == 'a':
            score = 2
        elif response == 'A':
            score = 3
    else:
        if response == 'D':
            score = 3
        elif response == 'd':
            score = 2
        elif response == 'a':
            score = 1
        elif response == 'A':
            score = 0

    total_score += score
    return total_score


def ask_questions(total_score):

    #questions

    print(
        '1. I feel that I am a person of worth, at least on an equal plane with others.'
    )
    total_score = answer(1, total_score)
    print('2. I feel that I have a number of good qualities.')
    total_score = answer(2, total_score)
    print('3. 3. All in all, I am inclined to feel that I am a failure.')
    total_score = answer(3, total_score)
    print('4. I am able to do things as well as most other people.')
    total_score = answer(4, total_score)
    print('5. I feel I do not have much to be proud of.')
    total_score = answer(5, total_score)
    print('6. I take a positive attitude toward myself.')
    total_score = answer(6, total_score)
    print('7. On the whole, I am satisfied with myself.')
    total_score = answer(7, total_score)
    print('8. I wish I could have more respect for myself.')
    total_score = answer(8, total_score)
    print('9. I certainly feel useless at times.')
    total_score = answer(9, total_score)
    print('10. At times I think I am no good at all.')
    total_score = answer(10, total_score)
    return total_score


main()