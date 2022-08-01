# Micro Lib to work with Film notes
import os
import pandas as pd

# Wrapper to store Film notes
__notes__ = pd.DataFrame
__file_path__ = 'example.csv'


def read_notes():
    # global needed to modify value of upper context variable in this method
    global __notes__
    if not os.path.exists(__file_path__):
        print('Please provide valid file path!')
    __notes__ = pd.read_csv(__file_path__)


def write_csv():
    # write existing Dataframe to the file
    __notes__.to_csv(__file_path__, index=False)
    # and reopen file
    read_notes()


def add_note(film_name, note, rating):
    global __notes__
    float_rating = 0
    try:
        float_rating = float(rating)
    except ValueError:
        print('Invalid rating input! Use numbers from 1 to 5.')
        return
    if float_rating < 1 or float_rating > 5:
        print('Invalid rating input! Use numbers from 1 to 5.')
        return
    buf_dataframe = pd.DataFrame([{'film_name': film_name, 'note': note, 'rating': float_rating}])
    __notes__ = pd.concat([__notes__, buf_dataframe]).reset_index(drop=True)
    write_csv()


def remove_note(note_index):
    global __notes__
    if note_index < 0 or note_index >= __notes__.size:
        print('Invalid index! Please select valid index value.')
        return
    __notes__ = __notes__.drop(note_index)
    write_csv()


def print_all():
    print('\nPrinting all notes:')
    print_notes(__notes__)


def print_notes(input_notes):
    print(input_notes.to_string())


def get_average_rating():
    return __notes__['rating'].mean().round(2)


def get_highest_5():
    return __notes__.sort_values(by='rating', ascending=False).reset_index(drop=True)[0:5]


def get_lowest_5():
    return __notes__.sort_values(by='rating', ascending=True).reset_index(drop=True)[0:5]
