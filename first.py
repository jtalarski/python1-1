"""
Name: Jim Talarski
Course: CIS189 16516
Module: 8
Topic: 2
Assignment: Unit Test Dictionary Assignment - test case file
"""


def average_scores(scores_dict):
    if len(scores_dict) >= 1:
        ld = len(scores_dict)
        s = sum(scores_dict.values())
        avg = s / ld
        print(f'Your dictionary of scores is: {scores_dict}')
        print(f'Your average score is: {avg:.2f}')
        return avg
    else:
        print(f'Your dictionary is empty {scores_dict}. We have a problem')
        raise ValueError

def get_test_scores():
    scores_dict = dict()
    good_input = False
    while not good_input:
        num_scores = input("How many scores would you like to enter? => ")
        try:
            int(num_scores)
            good_input = True
        except ValueError:
            print('You must enter a whole number, try again!')
        else:
            i = int(num_scores)
            x = 0
            for n in range(i):
                while x < i:
                    try:
                        score = input(
                            'What is the score you want to enter? => ')
                        int(score)
                    except ValueError:
                        print(
                            'You must enter a whole number greater than or equal to 1')
                    else:
                        x += 1
                        scores_dict.update({f'score {x}': int(score)})
            # return scores_dict
            average_scores(scores_dict)


if __name__ == '__main__':
    get_test_scores()
