list = [91, 7, 101, 6, 33, 19, 1, 0]
count = len(list)
done = False

# while done == False:
#     for i in range(0, count, 0, -1):
#         for 
#     done = True

'''
0  0000  0000
0     0  0  0
0  0000  0  0
0     0  0  0
0  0000  0000

Go through each list of numbers. Take the first number in the list and 
add that many '0's to the strings that will be the image. With each list 
you will be adding one character, either a '0' or a ' ', to each of 
the strings that will be the image pixels. After you add all the 
characters for the first number, you switch to adding ' ' for the next 
number. You switch back after that number until the first list is done.
Then you move to the next list and start this process again. When it is
all done, you should have a list of five equal length strings. Display
each of those strings on their own line.


main()
    row1 <- ''
    row2 <- ''
    row3 <- ''
    row4 <- ''
    row5 <- ''
    image <- [row1, row2, row3, row4, row5]
    fill <- True
    FOR each column in data
        current_row <- 0
        fill <- True
        FOR each num in column
            WHILE i < num
                IF fill = True
                    image[current_row] <- CONCAT(image[current_row], '0')
                ELSE
                    image[current_row] <- CONCAT(image[current_row], ' ')
                current_row <- current_row + 1
                i <- i + 1
            fill <- NOT fill
    FOR each row in image
        PUT row
            
Copilot's code was simpler, but it only works if the image is five rows
tall. That is also a failing of mine. I can see two possible solutions 
for fixing that. I can either get the amount of rows as input or I can
have new rows created as the program iterates. Copilot also did a better
job of initializing the variables than I did. The psuedocode I wrote
seems to match the algorithm in step one.

Update:
main()
    GET row_count
    GET data
    image <- []
    FOR i FROM 1 TO row_count
        APPEND(image, [])
    FOR EACH column IN data
        current_row <- 0
        fill <- True
        FOR each num in column
            i <- 0
            WHILE i < num
                IF fill = True
                    image[current_row] <- CONCAT(image[current_row], '0')
                ELSE
                    image[current_row] <- CONCAT(image[current_row], ' ')
                current_row <- current_row + 1
                i <- i + 1
            fill <- NOT fill
    FOR each row in image
        PUT row
        


main()
    moneyDollars <- getDollars()
    moneyEuroes = 0.873 * moneyDollars
    PUT moneyEuroes

displayNegative(balances)
    FOR i <- 0 ... balances.size()
        IF balances[i] < 0
            PUT error on the screen

isLeap(year)         
    IF year MOD 4 != 0
        PUT isn't a leap year
    ELSE
        IF year MOD 100 != 0
            PUT is a leap year
        ELSE
            IF year MOD 400 != 0
                PUT isn't a leap year
            ELSE
                PUT is a leap year

levelUp()
    if shipLevel = 2
        IF shipPoints >= 200
            IF minutesSinceLevelUp >= 2
                PUT level up to 3
            ELSE
                PUT need more time
        ELSE
            PUT need more points
    ELSE
        PUT must be level 2 first
'''

