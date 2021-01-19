def yearConvert(years):
    '''Takes years and prints, days, hours, minutes, seconds and returns seconds.'''
    
    # Use a try:/except: to catch non-numeric values of years
    try:
        days=365*float(years)
    except:
        print(f"Expecting a number for years, got {years}, a {type(years)}.")

    hours=24*days
    minutes=60*hours
    seconds=60*minutes

    print(f"{years} is:")
    print(f"   {days} days")
    print(f"   {hours} hours")
    print(f"   {minutes} minutes")
    print(f"   {seconds} seconds")

    return seconds

yearConvert(60)