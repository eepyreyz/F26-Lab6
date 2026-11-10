# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/9
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 
def times_ten(start_index, end_index):

    my_dictionary = dict()
    for i in range (start_index, end_index + 1):
        my_dictionary[i] = i*10 #1

    return my_dictionary


# TO DO 2: Run the script.
my_dictionary  = times_ten(2, 6)
print(my_dictionary)