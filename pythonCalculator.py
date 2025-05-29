import calendar

def is_leap(year):
    """Return True if leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def display_year_calendar(year):
    """Print the full calendar for the given year."""
    print("=" * 400)
    print(f"📅 Calendar for the year: {year}")
    print("=" * 400)
    print(calendar.TextCalendar(calendar.SUNDAY).formatyear(year, 2, 1, 1, 3))

def main():
    print("🗓  Welcome to the 400-Year Calendar Viewer 🗓")
    
    while True:
        try:
            start_year = int(input("Enter the start year (e.g., 1800): "))
            if start_year < 1:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid positive year (1 or higher).")

    end_year = start_year + 399
    print(f"\n✅ You can now view any year from {start_year} to {end_year}.")

    while True:
        try:
            selected_year = int(input("Enter the year you want to view: "))
            if selected_year < start_year or selected_year > end_year:
                raise ValueError
            break
        except ValueError:
            print(f"❌ Year must be between {start_year} and {end_year}.")

    display_year_calendar(selected_year)

if _name_ == "_main_":
    main()