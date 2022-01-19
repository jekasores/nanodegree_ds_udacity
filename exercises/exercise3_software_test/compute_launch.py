def days_until_launch(current_day, launch_day):
    '''Return the days left before launch
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    '''
    #Corrected/fixed solution - uncomment to check the difference in pytest
    #if launch_day-current_day < 0:
    #    return 0
    #else:
    #    return launch_day-current_day

    #____________________________________________

    #Original code without correction
    return launch_day-current_day