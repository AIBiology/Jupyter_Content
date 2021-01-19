for num in range(1,11):
    if (num % 2) == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    if num < 5:
        print(f"{num} is less than 5.")
    elif num == 5:
        print(f"{num} equals 5")
    else:
        print(f"{num} is greater than 5.")