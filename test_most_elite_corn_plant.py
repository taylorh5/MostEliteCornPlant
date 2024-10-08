import sys
import numpy as np
from most_elite_corn_plant import number_of_visible_stalks_row,number_of_visible_stalks_column,elite_corn_plants

SIMPLE_CORN_FIELD_ROWS = [          # By hand input of the simple 5x5 corn field to test the
    ["4", "1", "4", "8", "4"],      # most elite corn field code
    ["3", "6", "6", "2", "3"],
    ["7", "6", "4", "4", "3"],
    ["4", "4", "6", "5", "0"],
    ["4", "6", "4", "0", "1"],
]

SIMPLE_CORN_FIELD_COLUMNS = [       # By hand input of the simple 5x5 corn field to test the
    ["4", "1", "4", "8", "4"],      # most elite corn field code. The negatives are added
    ["3", "-6", "-6", "2", "3"],    # so we can make sure the code passes the test with the
    ["7", "-6", "4", "-4", "3"],    # correct array that would be passed in to the function.
    ["4", "4", "-6", "-5", "0"],
    ["4", "6", "4", "0", "1"],
]

# This tests the output of the number of visible stalks by rows from the left and right
def test_number_of_visible_stalks_row():
    corn_field = np.array(SIMPLE_CORN_FIELD_ROWS, dtype=int)
    visible_stalk_rows = number_of_visible_stalks_row(corn_field)
    assert visible_stalk_rows == 6

# This tests the output of the number of visible stalks by column both up and down
def test_number_of_visible_stalks_column():
    corn_field = np.array(SIMPLE_CORN_FIELD_COLUMNS, dtype=int)
    visible_stalk_column = number_of_visible_stalks_column(corn_field)
    assert visible_stalk_column == 0

# This tests the output of the most elite corn stalk. It test the field position, height, and elite score
def test_elite_corn_plants():
    corn_field = np.array(SIMPLE_CORN_FIELD_COLUMNS, dtype=int)
    debug=False
    row,column,most_elite,elite_height = elite_corn_plants(corn_field,debug)
    assert row == 3
    assert column == 2
    assert most_elite == 8
    assert elite_height == 6



