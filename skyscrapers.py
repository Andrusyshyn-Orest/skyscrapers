"""
GitHub repository: https://github.com/Andrusyshyn-Orest/skyscrapers

This module represents skyscrapers game.

>>> left_to_right_check("412453*", 4)
True
>>> left_to_right_check("452453*", 5)
False

>>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
'*?????5', '*?????*', '*?????*', '*2*1***'])
False
>>> check_not_finished_board(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_not_finished_board(['***21**', '412453*', '423145*',\
'*5?3215', '*35214*', '*41532*', '*2*1***'])
False

>>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
False
>>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*553215', '*35214*', '*41532*', '*2*1***'])
False

>>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
True
>>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
False
>>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
False
>>> check_horizontal_visibility(['***21**', '*24137', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
False

>>> check_columns(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
True
>>> check_columns(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41232*', '*2*1***'])
False
>>> check_columns(['***21**', '412553*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
False
"""


def read_input(path: str) -> list:
    """
    Read game board file from path.
    Return list of str.
    """

    check_lst = []
    with open(path, mode = 'r', encoding = 'UTF-8') as check:
        for row in check:
            check_lst.append(row.strip())
    return check_lst


def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """

    row = input_line[1:-1]
    max_height = row[0]
    visibility = 1
    for skyscraper in row:
        if skyscraper > max_height:
            max_height = skyscraper
            visibility += 1
    if visibility != pivot:
        return False
    return True


def check_not_finished_board(board: list) -> bool:
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
'*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
'*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    town = board[1:-1]
    for row in town:
        if '?' in row:
            return False
    return True


def check_uniqueness_in_rows(board: list) -> bool:
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    town = board[1:-1]
    length = len(town[0]) - 2
    for row in town:
        row = row[1:-1]
        if len(set(row)) != length:
            return False
    return True


def check_horizontal_visibility(board: list) -> bool:
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '*24137', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """

    town = board[1:-1]
    for row in town:
        left_hint, right_hint = row[0], row[-1]
        if left_hint != '*':
            if not left_to_right_check(row, int(left_hint)):
                return False

        if right_hint != '*':
            reversed_row = ''
            for skyscraper in row:
                reversed_row = skyscraper + reversed_row
            if not left_to_right_check(reversed_row, int(right_hint)):
                return False
    return True


def check_columns(board: list) -> bool:
    """
    Check column-wise compliance of the board for uniqueness
(buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """

    columns = []
    width = len(board[0])
    for col_ind in range(width):
        column = ''
        for row in board:
            column += row[col_ind]
        columns.append(column)

    if not check_uniqueness_in_rows(columns):
        return False

    if not check_horizontal_visibility(columns):
        return False

    return True


def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """

    board = read_input(input_path)
    if not check_not_finished_board(board):
        return False
    if not check_uniqueness_in_rows(board):
        return False
    if not check_horizontal_visibility(board):
        return False
    if not check_columns(board):
        return False
    return True


if __name__ == "__main__":
    import doctest
    #print(check_skyscrapers("check.txt"))
    print(doctest.testmod())
