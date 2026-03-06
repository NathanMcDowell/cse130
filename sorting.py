# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program sorts lists alphabetically
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out some bug with already sorted things being moved out of the sorted portion.
# 5. How long did it take for you to complete the assignment?
#      2 hours

'''
INPUT list
length <- LENGTH(list)
solved <- 0

FOR EACH IN list
    largest <- 0
    FOR i FROM 0 TO (length - solved)
        if list[i] > largest
            largest <- list[i]
            index_to_change <- i
    old_number <- list[length - solved]
    list[length - solved] <- largest
    list[index_to_change] <- old_number
    solved <- solved + 1


'''

import json

def main():
    file = input("Input file name: ")
    with open(file, "r") as filehandle:
        object = json.load(filehandle)
        list = object["array"]
    # print(list)
    length = len(list)
    # print(length)
    solved = 1
    for _ in range(length - 1):
        largest = list[0]
        index_to_change = 0
        for i in range(0, (length - solved)):
            if list[i] > largest:
                largest = list[i]
                index_to_change = i
        list[length - solved - 1], list[index_to_change] = \
        list[index_to_change], list[length - solved - 1]
        solved = solved + 1
        print(list)
    print(list)

main()

