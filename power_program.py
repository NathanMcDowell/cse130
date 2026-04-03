# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program checks which interval has the highest power level.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was coming up with all of the asserts.
# 5. How long did it take for you to complete the assignment?
#      This assignment took me about two hours

import json

def main():
    file = input('Input file name: ')
    try:
        with open(file, "r") as filehandle:
            power_array = json.load(filehandle)['array']
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except json.JSONDecodeError:
        raise ValueError("File is not valid JSON")
        
    
    assert all(isinstance(item, int) for item in power_array)
    assert all(item > 0 for item in power_array)

    subset_amount = int(input('Input subset size: '))

    assert subset_amount > 0
    assert subset_amount <= len(power_array)
    
    highest_subset = 0
    iterations = len(power_array) - subset_amount + 1
    for offset in range(iterations):
        curr_subset = 0
        for i in range(subset_amount):
            curr_subset += power_array[i + offset]
        if curr_subset >= highest_subset:
            highest_subset = curr_subset
    highest_avg_subset = highest_subset / subset_amount
    print(highest_avg_subset)


main()