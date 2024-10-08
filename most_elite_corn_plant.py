import sys
import numpy as np

# For easier debugging purposes
np.set_printoptions(threshold=sys.maxsize)  
np.set_printoptions(linewidth=500)  

###################################
# Functions
###################################


# Define fuction that will read in the corn stalk height from a given input file and return a 2D array with the corn stalk
# heights as string elements. This array "corn_field_string" will be used to determine the visible corn stalks and the most
# elite corn plant. This is converted to an array of integers in the driver.
def generate_corn_field(file, corn_field):

    # Open input file and read each line.
    # Then for each line we need to strip the '\n' so we don't have to deal with it as its own element in the array
    # We can then append the array "corn_field_string" with elements of each line, still as a string.
    # Leaving this loop we have the heights of each individual corn stalk as its own element of the array as a string. We need
    # each element to be a string in case there is a leading zero on any of the lines for any given input file. These leading
    # zero's will not stay if each line is read in as an integer first.
    with open(file, "r") as f:
        lines = f.readlines()
        for num, lines in enumerate(lines):
            lines = lines.strip("\n")
            corn_field_string.append(list(lines))


# Define fuction will flag all corn stalks visible along rows from both the right and left side. All visible stalks are flagged
# with a "-" sign in order for us to easily avoid double counting corn stalks. This also allows us to more easily debug as we
# can print the whole corn field array and see by the sign which stalks are visible from the row sides.


def number_of_visible_stalks_row(corn_field):
    # initialize our counter to zero. This accumulates the number of visible stalks viewed along rows
    visible_stalks_rows = 0  
    # Determine the number of rows and columns in our array/corn field for an general input file.
    nrow, ncol = np.shape(corn_field)  

    # In this loop we finish the loop before the last row and skip the first row to avoid double counting. All edge cases are
    # added first in the main driver code. The current tallest plant is set to be the first outer plant for the given row. We
    # start the loop over col at column index 1 since we are comparing the height of [row][0] with [row][1] to start. If the next
    # stalk in the loop is taller then we flag it and set the new tallest corn stalk on this row. We do not want to overcount.
    # This is more important for all subsequent parts, but if a stalk is already marked # as visible from another side of the
    # field, we want to skip over changing the sign and increasing our counter. If we have not "seen" this one so far, we will
    # flag its location with a "-" and increase our counter.
    for row in range(0, nrow - 1):
        if row != 0:
            current_tallest = corn_field[row][0]
            for col in range(1, ncol - 1):
                if abs(corn_field[row][col]) > abs(current_tallest):
                    current_tallest = abs(corn_field[row][col])
                    if corn_field[row][col] >= 0:
                        corn_field[row][col] = -corn_field[row][col]
                        visible_stalks_rows = visible_stalks_rows + 1

            # In this loop we check from right to left on the same row as above. The current tallest plant is set to be the last
            # outer plant for the same row with indexing from 0 to ncol-1. We start at the last column index and decrease as we
            # go since we are comparing the height of [row][ncol] with [row][ncol-1] to start. If the next stalk in the loop is taller
            # then we flag it and set the new tallest corn stalk on this row. We do not want to overcount. If a stalk is already marked
            # as visible from another side of the field, we want to skip over changing the sign and increasing our counter. If we
            # have not "seen" this one so far, we will flag its location with a "-" and increase our counter.
            current_tallest = corn_field[row][ncol - 1]
            for col in range(ncol - 1, 0, -1):
                if abs(corn_field[row][col]) > abs(current_tallest):
                    current_tallest = abs(corn_field[row][col])
                    if corn_field[row][col] >= 0:
                        corn_field[row][col] = -corn_field[row][col]
                        visible_stalks_rows = visible_stalks_rows + 1

    # Return coutner to main driver     
    return visible_stalks_rows  


# Define fuction will flag all corn stalks visible along columns from both the top and bottom. All visible stalks are flagged
# with a "-" sign in order for us to easily avoid double counting corn stalks. This is very important here since we have
# already encountered many visible stalks from the row sices. This also allows us to more easily debug as we can print the
# whole corn field array and see by the sign which stalks are visible as a whole.
def number_of_visible_stalks_column(corn_field):
    # initialize our counter to zero. This accumulates the number of visible stalks viewed along columns
    visible_stalks_column = 0 
    # Determine the number of rows and columns in our array/corn field
    nrow, ncol = np.shape(corn_field) 

    # In this loop we finish the loop before the last column and skip the first row to avoid double counting. All edge cases are
    # added first in the main driver code. The current tallest plant is set to be the first outer plant for the given column. We
    # start the loop over row at row index 1 since we are comparing the height of [0][col] with [1][col] to start. If the next
    # stalk in the loop is taller then we flag it and set the new tallest corn stalk on this column. We do not want to overcount.
    # As wit before, if a stalk is already marked as visible from another side of the field, we want to skip over changing
    # the sign and increasing our counter. If we have not "seen" this one so far, we will flag its location with a "-" and
    # increase our counter.
    for col in range(0, ncol - 1):
        if col != 0:
            current_tallest = corn_field[0][col]
            for row in range(1, nrow - 1):
                if abs(corn_field[row][col]) > abs(current_tallest):
                    current_tallest = abs(corn_field[row][col])
                    if corn_field[row][col] >= 0:
                        corn_field[row][col] = -corn_field[row][col]
                        visible_stalks_column = visible_stalks_column + 1

            # In this loop we check from bottom to top on the same column as above. The current tallest plant is set to be the last
            # outer plant for the same column with indexing from 0 to nrow-1. We start at the last row index and decrease as we
            # go since we are comparing the height of [nrow][col] with [nrow-1][col] to start. If the next stalk in the loop is taller
            # then we flag it and set the new tallest corn stalk on this column. We do not want to overcount. If a stalk is already
            # marked as visible from another side of the field, we want to skip over changing the sign and increasing our counter.
            # If we have not "seen" this one so far, we will flag its location with a "-" and increase our counter.
            current_tallest = corn_field[nrow - 1][col]
            for row in range(nrow - 1, 0, -1):
                if abs(corn_field[row][col]) > abs(current_tallest):
                    current_tallest = abs(corn_field[row][col])
                    if corn_field[row][col] >= 0:
                        corn_field[row][col] = -corn_field[row][col]
                        visible_stalks_column = visible_stalks_column + 1

    # Return coutner to main driver
    return visible_stalks_column  


# Define function that will find the most elite corn stalk and output its location (from index 1 for better user output).
def elite_corn_plants(corn_field, debug):
    # Determine the number of rows and columns in our array/corn field
    nrow, ncol = np.shape(corn_field)  

    # Initize our counter of the number of corn plants a given individual plant can see up a column, down a column, 
    # to the left on a row, o the right on a row, a variable to save the current elite corn score to be tested 
    # against the overall highest score, a variable to save the highest elite corn score up to that point, a variable 
    # to save the height of the most elite corn plant to print, and variables to store the location of the most elite 
    # corn plant to easily find its location in the field
    up = 0  
    down = 0 
    left = 0  
    right = 0  
    current_elite_number = 0  
    most_elite_so_far = 0
    elite_height = 0 
    row_save = 0  
    column_save = 0

    # Since all outer edge plants have an elite score of zero, we are going to start out on the second row with the
    # second column element. For each run over a given plant we need to re-zero the "left" counter. We need to start
    # with the value for "next_left" to be set just to the left of our current plant (col-1). In the case where our
    # current plant is neighbored by a plant of greater or equal height we increase the counter by 1 and move on.
    # If our plant is larger than its next neighbor, we increase our counter and move left until we hit a plant of
    # greater or equal height. Or we hit the start of the row with next_left=0. Then we exit the while() loop. If
    # we have hit one of our termination criteria, we still need to increase our counter by 1 more since this last
    # plant is still visible by our plant, but did not count the while loop.
    for row in range(0, nrow - 1):
        if row != 0:
            for col in range(0, ncol - 1):
                if col != 0:
                    left = 0
                    next_left = col - 1
                    if abs(corn_field[row][col]) <= abs(corn_field[row][next_left]):
                        left = left + 1
                    else:
                        while (
                            abs(corn_field[row][col]) > abs(corn_field[row][next_left])
                            and next_left >= 0
                        ):
                            left = left + 1
                            next_left = next_left - 1
                        if next_left >= 0 and abs(corn_field[row][col]) <= abs(
                            corn_field[row][next_left]
                        ):
                            left = left + 1

                    # Here we traverse to the right from our given plant. For each run over a given plant we need to re-zero the "right"
                    # counter. We need to start with the value for "next_right" to be set just to the right of our current plant (col+1).
                    # This loops runs the same as the previous loop, except we increase our next_right as +1 and we terminate our loop
                    # if we hit ncol-1 instead of 0.
                    right = 0
                    next_right = col + 1
                    if abs(corn_field[row][col]) <= abs(corn_field[row][next_right]):
                        right = right + 1
                    else:
                        while next_right <= ncol - 1 and abs(corn_field[row][col]) > abs(
                            corn_field[row][next_right]
                        ):
                            right = right + 1
                            next_right = next_right + 1
                        if next_right <= ncol - 1 and abs(corn_field[row][col]) <= abs(
                            corn_field[row][next_right]
                        ):
                            right = right + 1

                    # Here we traverse to the up from our given plant. For each run over a given plant we need to re-zero the "up"
                    # counter. We need to start with the value for "next_up" to be set just up of our current plant (row-1).
                    # This loops runs the same as the previous loop, except we decrease our next_up as -1 and we terminate our loop
                    # if we hit row=0.
                    up = 0
                    next_up = row - 1
                    if abs(corn_field[row][col]) <= abs(corn_field[next_up][col]):
                        up = up + 1
                    else:
                        while (
                            abs(corn_field[row][col]) > abs(corn_field[next_up][col])
                            and next_up >= 0
                        ):
                            up = up + 1
                            next_up = next_up - 1
                        if next_up >= 0 and abs(corn_field[row][col]) <= abs(
                            corn_field[next_up][col]
                        ):
                            up = up + 1

                    # Here we traverse to the down from our given plant. For each run over a given plant we need to re-zero the "down"
                    # counter. We need to start with the value for "next_down" to be set just down of our current plant (row+1).
                    # This loops runs the same as the previous loop, except we increase our next_down as +1 and we terminate our loop
                    # if we hit row=nrow-1.
                    down = 0
                    next_down = row + 1
                    if abs(corn_field[row][col]) <= abs(corn_field[next_down][col]):
                        down = down + 1
                    else:
                        while next_down <= nrow - 1 and abs(corn_field[row][col]) > abs(
                            corn_field[next_down][col]
                        ):
                            down = down + 1
                            next_down = next_down + 1
                        if next_down <= nrow - 1 and abs(corn_field[row][col]) <= abs(
                            corn_field[next_down][col]
                        ):
                            down = down + 1

                    # Here we calculate this plants elite corn score. We want the most elite corn plant. So if our current plant's score
                    # is higher, we want to know. If our plant is the most elite so far, we want to store that information. We can print
                    # this as we go for debugging. Otherwise, once the full field has been traversed we have all our information saved
                    # on our most elite corn plant.
                    current_elite_number = left * right * up * down
                    if current_elite_number > most_elite_so_far:
                        most_elite_so_far = current_elite_number
                        row_save = row
                        column_save = col
                        elite_height = abs(corn_field[row][col])
                        if debug is True:
                            print(
                                "Most Elite so far is (",
                                row + 1,
                                ",",
                                col + 1,
                                ") =",
                                most_elite_so_far,
                            )
    # Return the row,column position for the most elite corn plant, the elite score, and the height of the most elite plant.
    return (
        row_save,
        column_save,
        most_elite_so_far,
        elite_height,
    )  


###################################################################
# Main Driver Code
###################################################################

print("####################################")
print("# Elite Corteva Corn Plants Solver #")
print("####################################")


# Set file location to read in the following lines. 
file = "/Users/taylorharville/Desktop/Corteva_Coding_Test/input.txt"

# Debug flag that print more information not useful to end user, but helpful for the developer
debug = False

# Allocate the array to store the string elements of the input file and the final integer array we will work on
corn_field = []
corn_field_string = []

# This generates the array of string elements read in from our file. This is done by strings to keep the leading zero's.
generate_corn_field(file, corn_field_string)

# Modify each element of our array to be in integer rather than string. Now we will keep any leading zero's.
corn_field = np.array(corn_field_string, dtype=int)
if debug is True:
    print(np.array(corn_field))

# Begin with taking all field edge cases. The "-4" deals with double counting of corner cases
# Determine the number of rows and columns in our array/corn field
nrow, ncol = np.shape(corn_field)  
visible_stalks_outer = nrow + nrow + ncol + ncol - 4
print("Outer Stalks =", visible_stalks_outer)


# Find the visible plants by row.
visible_stalks_rows = number_of_visible_stalks_row(corn_field)
if debug is True:
    print("Corn field visible by rows")
    print(np.array(corn_field))
    print("Outer + Row Stalks =", visible_stalks_outer + visible_stalks_rows)


# Find the visible plants by column.
visible_stalks_column = number_of_visible_stalks_column(corn_field)
if debug is True:
    print("Corn field visible by rows and columns")
    print(np.array(corn_field))

# Print relevant information along our search for the number of visible plants.
print("Stalks Visible by Row=", visible_stalks_rows)
print("Additional Stalks Visible by Column=", visible_stalks_column)
print(
    "Total Visible Stalks =",
    visible_stalks_outer + visible_stalks_rows + visible_stalks_column,
)

# Find the most elite corn plant
row, column, most_elite, elite_height = elite_corn_plants(corn_field, debug)

# Print relevant information along our search for the most elite corn plant. We add the +1 to row and column
# to convert the 0 indexed numbers to 1. This tends to be more non-developer friendly format.
print(
    "Most Elite Corn Plant is at (row=",
    row + 1,
    ",column=",
    column + 1,
    ") with height of:",
    elite_height,
    " and an Elite Score of:",
    most_elite,
)
