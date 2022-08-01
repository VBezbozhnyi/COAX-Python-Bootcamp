# Create micro library that allows users to work with notes about ukrainian films.
# Note should contain film_name, note, rating (rating - is 1 - 5 rating of the film)
# Micro lib should contain the next functionality:
#
#     Read notes from .csv file
#     Add note to .csv file
#     Remove note from .csv file
#     Print notes to console
#     Get films with the highest rating
#     Get films with the lowest rating
#     Get average rating among all films
import micro_lib
import os


def print_actions():
    print('0: Exit')
    print('1: Print all notes')
    print('2: Print highest rating')
    print('3: Print lowest rating')
    print('4: Show average rating')
    print('5: Add note')
    print('6: Remove note')


if __name__ == '__main__':
    # first read all notes from file
    micro_lib.read_notes()
    # and print them
    micro_lib.print_all()
    # enter control loop
    while True:
        os.system('clear')
        print('\n\nChoose action (only integers are allowed):')
        print_actions()
        action = input('Input here:')
        if not action.isnumeric():
            print('WRONG ACTION. Please use only numbers!')
            continue
        action_code = int(action)
        if action_code not in [0, 1, 2, 3, 4, 5, 6]:
            print('WRONG ACTION')
        elif action_code == 0:
            print('Exiting...')
            break
        elif action_code == 1:
            micro_lib.print_all()
        elif action_code == 2:
            print('\nHighest rating')
            micro_lib.print_notes(micro_lib.get_highest_5())
        elif action_code == 3:
            print('\nLowest rating')
            micro_lib.print_notes(micro_lib.get_lowest_5())
        elif action_code == 4:
            print('\nAverage rating: ', micro_lib.get_average_rating())
        elif action_code == 5:
            print('Please enter:\n')
            micro_lib.add_note(input('Film name:'), input('Note:'), input('Rating:'))
        elif action_code == 6:
            micro_lib.print_all()
            index = input('Please pass index of a note you want to be removed:')
            if not index.isnumeric():
                print('Please use only numbers!')
                continue
            micro_lib.remove_note(int(index))
