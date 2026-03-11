'''
Run a loop dependent onthe two dates not being equal. In the loop, check if the years
are the same if they are't, add to the day counter until the year is finished.
If/once they are the same, do a similar process for the month, then the day.

---------------------------------------------------------------------------------------
GET s_day, s_month, s_year
GET e_day, e_month, e_year

day_count <- 0

while (s_day, s_month, s_year) != (e_day, e_month, e_year):
    if s_year == e_year:
        if s_month == e_month:
            while s_day < e_day:
                day_count <- day_count + 1

        else if month == 1, 3, 5, 7, 8, 10, 12:
            while s_day <= 31:
                day_count <- day_count + 1
            s_day <- 1
            s_month <- s_month + 1
        else if month == 4, 6, 9, 11:
            while s_day <= 30:
                day_count <- day_count + 1
            s_day <- 1
            s_month <- s_month + 1
        else if month == 2:
            if is_lead_year():
                while s_day <= 29:
                    day_count <- day_count + 1
                s_day <- 1
                s_month <- s_month + 1
            else:
                while s_day <= 28:
                    day_count <- day_count + 1
                s_day <- 1
                s_month <- s_month + 1
    else:
        while s_year < end_year:
            while s_month <= 12:
                else if month == 1, 3, 5, 7, 8, 10, 12:
                    while s_day <= 31:
                        day_count <- day_count + 1
                    s_day <- 1
                    s_month <- s_month + 1
                else if month == 4, 6, 9, 11:
                    while s_day <= 30:
                        day_count <- day_count + 1
                    s_day <- 1
                    s_month <- s_month + 1
                else if month == 2:
                    if is_lead_year():
                        while s_day <= 29:
                            day_count <- day_count + 1
                        s_day <- 1
                        s_month <- s_month + 1
                    else:
                        while s_day <= 28:
                            day_count <- day_count + 1
                        s_day <- 1
                        s_month <- s_month + 1
            if is_leap_year() == false:
                day_count <- day_count + 365
            else:
                day_count <- day_count + 366

-----------------------------------------------------------------------------------                
Copilot Solution:
INPUT: date1 (year1, month1, day1)
       date2 (year2, month2, day2)

day_count ← 0

WHILE (year1 ≠ year2) OR (month1 ≠ month2) OR (day1 ≠ day2):

    // Step 1: Fix the year
    IF year1 ≠ year2:
        // Add days until date1 reaches the end of its year
        day_count ← day_count + 1
        INCREMENT date1 by 1 day
        CONTINUE LOOP

    // Step 2: Fix the month (years now match)
    IF month1 ≠ month2:
        day_count ← day_count + 1
        INCREMENT date1 by 1 day
        CONTINUE LOOP

    // Step 3: Fix the day (years and months now match)
    IF day1 ≠ day2:
        day_count ← day_count + 1
        INCREMENT date1 by 1 day
        CONTINUE LOOP

END WHILE

OUTPUT day_count
------------------------------------------------------------------------------------
Compare and Contrast
The AI did things much more simply than me. It used increment, which is helpful.
Copilot's code seems to be too simple. It doesn't explain any of the logic that goes
into adding days repeatedly. I mentioned leap years in my approach and it didn't 
mention them. I suppose my approach ended up being simpler to say than it was to code.

------------------------------------------------------------------------------------
Update

INPUT: s_day, s_month, s_year
INPUT:  e_day, e_month, e_year

day_count <- 0 # A

WHILE (s_day, s_month, s_year) != (e_day, e_month, e_year):
    IF s_year == e_year:
        IF s_month == e_month:
            WHILE s_day < e_day:
                INCREMENT day_count
            # B
        ELSE IF month == 1, 3, 5, 7, 8, 10, 12:
            WHILE s_day <= 31:
                INCREMENT day_count
            s_day <- 1
            INCREMENT s_month # C

        ELSE IF month == 4, 6, 9, 11:
            WHILE s_day <= 30:
                INCREMENT day_count
            s_day <- 1
            INCREMENT s_month # D

        ELSE IF month == 2:
            IF is_lead_year():
                WHILE s_day <= 29:
                    INCREMENT day_count
                s_day <- 1
                INCREMENT s_month # E
            ELSE:
                WHILE s_day <= 28:
                    INCREMENT day_count
                s_day <- 1
                INCREMENT s_month # F
    ELSE:
        WHILE s_year < end_year:
            WHILE s_month <= 12:
                IF month == 1, 3, 5, 7, 8, 10, 12:
                    WHILE s_day <= 31:
                        INCREMENT day_count
                    s_day <- 0
                    INCREMENT s_month # G
                    
                ELSE IF month == 4, 6, 9, 11:
                    WHILE s_day <= 30:
                        INCREMENT day_count
                    s_day <- 0
                    INCREMENT s_month # H
                    
                ELSE IF month == 2:
                    IF is_lead_year():
                        WHILE s_day <= 29:
                            INCREMENT day_count
                        s_day <- 0
                        INCREMENT s_month # I
                    ELSE:
                        WHILE s_day <= 28:
                            INCREMENT day_count
                        s_day <- 0
                        INCREMENT s_month # J
            s_month <- 1
            INCREMENT s_year # K
            END WHILE
        END WHILE
END WHILE
-------------------------------------------------------------------------

Efficiency
The efficiency is O(n) because the time taken to calculate the difference
increases linearly as the dates get further apart.


Step 1 By Hand: 4 minutes
Step 2 Approach: 8 minutes
Step 3 Pseudocode: 20 minutes
Step 4 Copilot: 2 minutes
Step 5 Compare and Contrast: 5 minutes
Step 6 Update: 15 minutes
Step 7 Trace: 31 minutes
Step 8 Efficiency: 2 minutes
'''

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_number_of_days_preset(s_day, s_month, s_year, e_day, e_month, e_year):
    print(f"Start Day: {s_day}.{s_month}.{s_year} - End Day: {e_day}.{e_month}.{e_year}")

    
    assert all(isinstance(i, int) for i in (s_day, s_month, s_year, e_day, e_month, e_year)), "All inputs must be integers"
    assert s_year > 1753, "Start year too early"


    day_count = 0

    while (s_day, s_month, s_year) != (e_day, e_month, e_year):
        if s_year == e_year:
            if s_month == e_month:
                while s_day < e_day:
                    day_count += 1
                    s_day += 1
                # B
            elif s_month in (1, 3, 5, 7, 8, 10, 12):
                while s_day <= 31:
                    day_count += 1
                    s_day += 1
                s_day = 1
                s_month += 1 # C

            elif s_month in (4, 6, 9, 11):
                while s_day <= 30:
                    day_count += 1
                    s_day += 1
                s_day = 1
                s_month += 1 # D

            elif s_month == 2:
                if is_leap_year(s_year):
                    while s_day <= 29:
                        day_count += 1
                        s_day += 1
                    s_day = 1
                    s_month += 1 # E
                else:
                    while s_day <= 28:
                        day_count += 1
                        s_day += 1
                    s_day = 1
                    s_month += 1 # F
        else:
            while s_year < e_year:
                while s_month <= 12:
                    if s_month in (1, 3, 5, 7, 8, 10, 12):
                        while s_day <= 31:
                            day_count += 1
                            s_day += 1
                        s_day = 1
                        s_month += 1 # G
                        
                    elif s_month in (4, 6, 9, 11):
                        while s_day <= 30:
                            day_count += 1
                            s_day += 1
                        s_day = 1
                        s_month += 1 # H
                        
                    elif s_month == 2:
                        if is_leap_year(s_year):
                            while s_day <= 29:
                                day_count += 1
                                s_day += 1
                            s_day = 1
                            s_month += 1 # I
                        else:
                            while s_day <= 28:
                                day_count += 1
                                s_day += 1
                            s_day = 1
                            s_month += 1 # J
                s_month = 1
                s_year += 1 # K
    print(f"Day Count: {day_count}")


def calculate_number_of_days():
    s_day = int(input("Start day: "))
    s_month = int(input("Start month: "))
    s_year = int(input("Start year: "))

    e_day = int(input("End day: "))
    e_month = int(input("End month: "))
    e_year = int(input("End year: "))

    day_count = 0

    while (s_day, s_month, s_year) != (e_day, e_month, e_year):
        if s_year == e_year:
            if s_month == e_month:
                while s_day < e_day:
                    day_count += 1
                    s_day += 1
                # B
            elif s_month in (1, 3, 5, 7, 8, 10, 12):
                while s_day <= 31:
                    day_count += 1
                    s_day += 1
                s_day = 1
                s_month += 1 # C

            elif s_month in (4, 6, 9, 11):
                while s_day <= 30:
                    day_count += 1
                    s_day += 1
                s_day = 1
                s_month += 1 # D

            elif s_month == 2:
                if is_leap_year():
                    while s_day <= 29:
                        day_count += 1
                        s_day += 1
                    s_day = 1
                    s_month += 1 # E
                else:
                    while s_day <= 28:
                        day_count += 1
                        s_day += 1
                    s_day = 1
                    s_month += 1 # F
        else:
            while s_year < e_year:
                while s_month <= 12:
                    if s_month in (1, 3, 5, 7, 8, 10, 12):
                        while s_day <= 31:
                            day_count += 1
                            s_day += 1
                        s_day = 0
                        s_month += 1 # G
                        
                    elif s_month in (4, 6, 9, 11):
                        while s_day <= 30:
                            day_count += 1
                            s_day += 1
                        s_day = 0
                        s_month += 1 # H
                        
                    elif s_month == 2:
                        if is_leap_year():
                            while s_day <= 29:
                                day_count += 1
                                s_day += 1
                            s_day = 0
                            s_month += 1 # I
                        else:
                            while s_day <= 28:
                                day_count += 1
                                s_day += 1
                            s_day = 0
                            s_month += 1 # J
                s_month = 1
                s_year += 1 # K
    print(f"Day Count: {day_count}")

calculate_number_of_days_preset(9, 1, "banana", 27, 5, 2028)
# calculate_number_of_days_preset(17, 11, 2002, 6, 4, 2004) # Previous week's test
# calculate_number_of_days_preset(9, 1, 2001, 9, 1, 2001) 
# calculate_number_of_days_preset(9, 1, 2001, 19, 1, 2001) 
# calculate_number_of_days_preset(9, 1, 2001, 19, 4, 2001)
# calculate_number_of_days_preset(9, 1, 2001, 6, 10, 2003)
# calculate_number_of_days_preset(9, 1, 2001, 27, 5, 2028)
