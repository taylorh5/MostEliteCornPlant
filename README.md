# MostEliteCornPlant
This code repository contains the code to find the most elite corn plant in a field.

most_elite_corn_plant.py is the main executable to find out a number of important things about a given corn field. It will give the number of visible
corn plants from all sides of the field. It will also give you the elite corn plant's location, height, and elite score. 

test_most_elite_corn_plant.py contains the unit tests for the functions defined in most_elite_corn_plant.py

small_input.txt is a 5x5 field size for testing.
10.input.txt is a 10x10 field size for testing.
input.txt is the production level input field. 

Any non-jagged corn field can be read in and used to find the most elite corn field. 

To run the code: python /path/to/directory/most_elite_corn_plant.py

The path to the file must be edited by changing:

file = "/Users/taylorharville/Desktop/Corteva_Coding_Test/input.txt""

to 

file = "/path/to/your/directory/input.txt"

To run the test with pytest: python -m pytest test_most_elite_corn_plant.py




