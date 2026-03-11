
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_number_of_days_preset(s_day, s_month, s_year, e_day, e_month, e_year):
    print(f"Start Day: {s_day}.{s_month}.{s_year} - End Day: {e_day}.{e_month}.{e_year}")

    
    assert all(isinstance(i, int) for i in (s_day, s_month, s_year, e_day, e_month, e_year)), "All inputs must be integers"
    assert s_year > 1753, "Start year too early"
    assert s_day > 0, "Day cannot be 0"
    assert s_month > 0, "Month cannot be less than 1"
    assert s_month < 13, "Month cannot be greater than 12"
    if s_year > e_year:
        assert False,"Start day cannot be after end day"
    elif s_year == e_year:
        if s_month > e_month:
            assert False,"Start day cannot be after end day"
        elif s_month == e_month:
            if s_day > e_day:
                assert False,"Start day cannot be after end day"
    if s_month in (1, 3, 5, 7, 8, 10, 12):
        if s_day > 31:
            assert False, "Too many days for that month"
    elif s_month in (4, 6, 9, 11):
        if s_day > 30:
            assert False, "Too many days for that month"
    else:
        if is_leap_year(s_year) == False:
            if s_day > 28:
                assert False, "Too many days for that month"
        else:
            if s_day > 29:
                assert False, "Too many days for that month"
    if e_month in (1, 3, 5, 7, 8, 10, 12):
        if e_day > 31:
            assert False, "Too many days for that month"
    elif e_month in (4, 6, 9, 11):
        if e_day > 30:
            assert False, "Too many days for that month"
    else:
        if is_leap_year(e_year) == False:
            if e_day > 28:
                assert False, "Too many days for that month"
        else:
            if e_day > 29:
                assert False, "Too many days for that month"
                

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


# calculate_number_of_days_preset(9, 1, 1752, 27, 5, 2028)
# calculate_number_of_days_preset(9, 1, "banana", 27, 5, 2028)
# calculate_number_of_days_preset(9, 0, 2001, 27, 5, 2028)
# calculate_number_of_days_preset(9, 13, 2001, 27, 5, 2028)
# calculate_number_of_days_preset(0, 12, 2001, 27, 5, 2028)
calculate_number_of_days_preset(29, 2, 2003, 27, 5, 2028)
calculate_number_of_days_preset(9, 1, 2001, 8, 1, 2001) #January 9, 2001, January 8, 2001
calculate_number_of_days_preset(17, 11, 2002, 6, 4, 2004) # Previous week's test
calculate_number_of_days_preset(9, 1, 2001, 9, 1, 2001) 
calculate_number_of_days_preset(9, 1, 2001, 19, 1, 2001) 
calculate_number_of_days_preset(9, 1, 2001, 19, 4, 2001)
calculate_number_of_days_preset(9, 1, 2001, 6, 10, 2003)
calculate_number_of_days_preset(9, 1, 2001, 27, 5, 2028)
