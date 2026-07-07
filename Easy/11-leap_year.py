# Check whether a given year is a leap year.

# Get year from the user.
year = int(input("Enter a year: "))

# Check leap year conditions.
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")