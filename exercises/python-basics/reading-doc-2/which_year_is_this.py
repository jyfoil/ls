from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# The Python documentation for the datetime module provides two attributes 
# to retrieve the year from a date or datetime object: year and isocalendar.

# What is the difference between the year attribute and the isocalendar method?

print(today_year)
print(iso_year)

# The year attribute of a date or datetime object simply returns the year of that date.

# The isocalendar method returns a tuple containing three values: the ISO year, ISO week number, and ISO weekday. 
# The ISO year (isocalendar()[0]) may differ from the Gregorian calendar year (year) for dates close to the start or end of the year, 
# because the ISO year starts with the first week that has at least 4 days in the new year.

