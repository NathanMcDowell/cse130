# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program checks to see if it is possible to put a hotel on Pennsylvania Ave in Monopoly. If it is, the program tells you how to do it.
# 4. What was the hardest part? Be as specific as possible.
#      I think that the hardest part was figuring out how to make all the different outcomes fit together cleanly. I mean that it was hard to organize this project.
#       I ended up not worrying too much about it and focused on getting the code running. It was helpful to have all of the inputs and outputs in the instructions.
#       That made it much easier to figure out what problems I needed to solve and the parts I had to work with.
#      
# 5. How long did it take for you to complete the assignment?
#      It took me about three hours to complete this assignment.

def main():   
    owns_all_green = input("Do you own all of the green properties? (y/n) ")
    if owns_all_green == "y":
        pacific_avenue_houses = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        north_carolina_houses = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        pennsylvania_avenue_houses = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if pacific_avenue_houses < 5:
            pacific_houses_needed = 4 - pacific_avenue_houses
        else:
            pacific_houses_needed = 0

        if north_carolina_houses < 5:
            north_carolina_houses_needed = 4 - north_carolina_houses
        else:
            north_carolina_houses_needed = 0

        if pennsylvania_avenue_houses < 4:
            pennsylvania_houses_needed = 4 - pennsylvania_avenue_houses
            total_houses_needed = pennsylvania_houses_needed + north_carolina_houses_needed + pacific_houses_needed
            houses_for_purchase = int(input("How many houses are there to purchase? "))
            hotels_for_purchase = int(input("How many hotels are there to purchase? "))
            if houses_for_purchase >= total_houses_needed:
                if hotels_for_purchase > 0:
                    total_cash_needed = 200 + 200 * total_houses_needed
                    user_cash = int(input("How much cash do you have to spend? "))
                    if user_cash >= total_cash_needed:
                        print(f"This will cost ${total_cash_needed}.")
                        print(f"Purchase 1 hotel and {total_houses_needed} houses.")
                        print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
                        if pacific_houses_needed > 0:
                            print(f"Put {pacific_houses_needed} house(s) on Pacific.")
                        if north_carolina_houses_needed > 0:
                            print(f"Put {north_carolina_houses_needed} house(s) on North Carolina.")
                    else:
                        print("You do not have sufficient funds to purchase a hotel at this time.")
                else:
                    print("There are not enough hotels available for purchase at this time.")
            else:
                print("There are not enough houses available for purchase at this time.")
        elif pennsylvania_avenue_houses == 4:
            if pacific_avenue_houses == 5:
                print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
            elif north_carolina_houses == 5:
                print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
            else:
                total_houses_needed = north_carolina_houses_needed + pacific_houses_needed
                houses_for_purchase = int(input("How many houses are there to purchase? "))
                hotels_for_purchase = int(input("How many hotels are there to purchase? "))
                if houses_for_purchase >= total_houses_needed:
                    if hotels_for_purchase > 0:
                        total_cash_needed = 200 + 200 * total_houses_needed
                        user_cash = int(input("How much cash do you have to spend? "))
                        if user_cash >= total_cash_needed:
                            print(f"This will cost ${total_cash_needed}.")
                            print(f"Purchase 1 hotel and {total_houses_needed} houses.")
                            print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
                            if pacific_houses_needed > 0:
                                print(f"Put {pacific_houses_needed} house(s) on Pacific.")
                            if north_carolina_houses_needed > 0:
                                print(f"Put {north_carolina_houses_needed} house(s) on North Carolina.")
                        else:
                            print("You do not have sufficient funds to purchase a hotel at this time.")
                    else:
                        print("There are not enough hotels available for purchase at this time.")
                else:
                    print("There are not enough houses available for purchase at this time.")
        else:
            print("You cannot purchase a hotel if the property already has one.")
    else:
        print("You cannot purchase a hotel until you own all the properties of a given color group.")

    




main()