def programming_left(days_working, total_days):
    print "\nYou have been at this for %d days" % days_working
    print "\nThe total number of days you had available was %d" % total_days
    print "\nYou still have %d left to get your shit together" % (total_days - days_working)

days_working = int(raw_input("How many days have you been at this?\n>>"))
total_days = 100
programming_left(days_working, total_days)