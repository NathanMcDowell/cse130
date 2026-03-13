
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def complete_month(day_count, day, month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month in (4, 6, 9, 11):
        days = 30
    else: # February
        if not is_leap_year(year):
            days = 28
        else:
            days = 29
    while day <= days:
        day_count += 1
        day += 1
    day = 1
    month += 1
    return day_count, day, month, year

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
        if not is_leap_year(s_year):
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
        if not is_leap_year(e_year):
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
            else:
                day_count, s_day, s_month, s_year = \
                complete_month(day_count, s_day, s_month, s_year)
        else:
            while s_year < e_year:
                while s_month <= 12:
                    day_count, s_day, s_month, s_year = \
                    complete_month(day_count, s_day, s_month, s_year)
                s_month = 1
                s_year += 1 # K
    print(f"Day Count: {day_count}")


# calculate_number_of_days_preset(9, 1, 1752, 27, 5, 2028)
# calculate_number_of_days_preset(9, 1, "banana", 27, 5, 2028)
# calculate_number_of_days_preset(9, 0, 2001, 27, 5, 2028)
# calculate_number_of_days_preset(9, 13, 2001, 27, 5, 2028)
# calculate_number_of_days_preset(0, 12, 2001, 27, 5, 2028)
# calculate_number_of_days_preset(29, 2, 2003, 27, 5, 2028)
# calculate_number_of_days_preset(9, 1, 2001, 8, 1, 2001) # January 9, 2001, January 8, 2001
calculate_number_of_days_preset(9, 1, 2001, 9, 1, 2001) 
calculate_number_of_days_preset(9, 1, 2001, 19, 1, 2001) 
calculate_number_of_days_preset(9, 1, 2001, 19, 4, 2001)
calculate_number_of_days_preset(9, 1, 2001, 6, 10, 2003)
calculate_number_of_days_preset(9, 1, 2001, 27, 5, 2028)
