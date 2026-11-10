# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date:
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

# TO DO 1: Copy the code from lab5b.py and paste here.
# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.



def s3_and_s5_not_s7(set3,set5,set7):
    set3andset5 = set3 & set5 # get them both
    set3andset5_not7 = set3andset5.difference(set7) 
    return set3andset5_not7

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

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s3and5_not7 = s3_and_s5_not_s7(s3,s5,s7)
    print(s3and5_not7)

main()


