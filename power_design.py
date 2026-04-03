'''
Step 2: Approach
You take the list of numbers and the subset amount as variables. Then you run a loop that adds 
numbers from the list until it reaches the subset amount. Then you make a highest value
variable and assign it to that. You do this loop over again, replacing the highest value
as new subsets break the record. At the end you divide the highest value by the subset
amount to get the highest average subset.

Step 3: Pseudocode

INPUT power_set, subset_amount

curr_subset <- 0
highest_subset <- 0
offset <- 0
iterations <- LENGTH(power_set) - subset_amount
FOR i in RANGE(iterations):
    curr_subset <- 0
    FOR i IN RANGE(subset_amount)
        curr_subset <- curr_subset + power_set[i + offset]
    END FOR
    IF curr_subset >= highest_subset:
        highest_subset <- curr_subset
    END IF
    offset += 1
END FOR
highest_avg_subset <- highest_subset / subset_amount
OUTPUT highest_avg_subset

Step 4: Microsoft Copilot
INPUT: numbers_list, subset_size

highest_total ← 0
current_total ← 0
index ← 0

// Loop until we run out of numbers
WHILE index < LENGTH(numbers_list)

    current_total ← 0
    count ← 0

    // Build one subset by adding numbers until we reach subset_size
    WHILE index < LENGTH(numbers_list) AND count < subset_size
        current_total ← current_total + numbers_list[index]
        index ← index + 1
        count ← count + 1
    END WHILE

    // If this subset breaks the record, store it
    IF current_total > highest_total
        highest_total ← current_total
    END IF

END WHILE

// Compute the highest average
highest_average ← highest_total / subset_size

OUTPUT highest_average

Step 5: Compare and Contrast
Both mine and Copilot's solutions seem to work. They are about the same length.
As always, Copilot knows psuedocode syntax better than I do. Looking closely, I think
it actually made a mistake. The mistake is my bad since I didn't make my approach very
clear.

Step 6: Update
INPUT power_set, subset_amount

curr_subset <- 0
highest_subset <- 0
iterations <- (LENGTH(power_set) - subset_amount) + 1
FOR offset in RANGE(iterations):
    curr_subset <- 0 #A
    FOR i IN RANGE(subset_amount)
        curr_subset <- curr_subset + power_set[i + offset] #B
    END FOR
    IF curr_subset >= highest_subset:
        highest_subset <- curr_subset
    END IF
END FOR
highest_avg_subset <- highest_subset / subset_amount
OUTPUT highest_avg_subset #C

Step 7: Trace
Create a program trace of the algorithm which computes the data below with a sub-list of size 4.

41	45	47	32	49	40	32
Step 8: Efficiency
This algorithm's efficiency is O(n + m) because the amount of computing needed increases
linearly as the data increases and because there are two inputs that impact the processing.

Step 1 By Hand: 7 minutes
Step 2 Approach: 6 minutes
Step 3 Pseudocode: 12 minutes
Step 4 Copilot: 2 minutes
Step 5 Compare and Contrast: 5 minutes
Step 6 Update: 6 minutes
Step 7 Trace: 16 minutes
Step 8 Efficiency: 2 minutes
'''