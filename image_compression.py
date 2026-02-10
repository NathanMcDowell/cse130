# 1. Name:
#       Nathan McDowell
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This program reads a compressed image from a file and prints the image.
# 4. Algorithmic Efficiency
#      The efficiency is O(n + m) because it linearly gets bigger as the input value gets bigger, and there are two input values.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out the O notation since it input two values. I did
#       a bit of research and I was able to figure it out.
# 6. How long did it take for you to complete the assignment?
#      About an hour and a half.

import json

def main():
    file = input("Input file name: ")
    with open(file, "r") as filehandle:
        compressed_data = json.load(filehandle)
    row_count = compressed_data["num_rows"]
    image = []
    for _ in range(row_count):
        image.append("")
    for column in compressed_data["data"]:
        current_row = 0
        fill = True
        for num in column:
            for _ in range(num):
                if fill:
                    image[current_row] = image[current_row] + "0"
                else:
                    image[current_row] = image[current_row] + " "
                current_row = current_row + 1
            fill = not fill
    for row in image:
        print(row)

main()