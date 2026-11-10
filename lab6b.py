# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/9
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py
# TO DO 1: Copy the code from lab6a.py and paste here.
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.


def s3ors5(set1,set2):

    union_set = set1 | set2 # get them both
    intersection_set = set1.intersection(set2) #get only whats in them both

    # subtract the union list that has them both from the intersection that has only shared elements
    diffrence_list = union_set.difference(intersection_set)

    return diffrence_list

def buildtheSet(divisor):
    numbers = set()

    for num in range(0, 101):
        if num % divisor == 0:
            numbers.add(num)
    return numbers

def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s3or5 = s3ors5(s3,s5)
    print(s3or5)

main()

