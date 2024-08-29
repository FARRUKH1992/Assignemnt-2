# a year is a leap year if divisible by 4
# a year divisible by 100 is not leap year
# a year is also divisible by 400 is leap year

def is_leap_year(year):
    """Determine if a given year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    # Prompt for input
    year = int(input("Enter a year: "))
    
    # Determine if the year is a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# make sure code works when run
if __name__ == "__main__":
    main()