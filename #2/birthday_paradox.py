# birthday_paradox.py - Tags: short, math, simulation.


import random, datetime


def get_birthdays(no_of_birthdays):
    """Returns a list of random date objects for birthdays."""
    birthdays = []
    for i in range(no_of_birthdays):

        # The year is unimportant for our simulation, as long as all birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day in a year.
        random_number_of_days = datetime.timedelta(random.randint(1, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthday list."""
    if len(birthdays) == len(set(birthdays)):
        # All birthdays are unique, so return None.
        return None

    # Compare each birthday to every other birthday.
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                # Return the matching birthday.
                return birthday_a


# Display the intro.
print(
    """Birthday Paradox
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them having matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.)

    (It's not actually a paradox, it's just a suprising result."""
)

# Set up a tuple of month names in order.
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

# Keep asking until the user enters a valid amount.
while True:
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_b_days = int(response)
        # The user has entered a valid amount.
        break
print()

# Generate and display the birthdays.
print(f"Here are, {num_b_days}, birthdays.")
birthdays = get_birthdays(num_b_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end="")
        month_name = MONTHS[birthday.month - 1]
        date_text = f"{month_name} {birthday.day}"
        print(date_text, end="")
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results.
print("In this simulation, ", end="")
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print(f"multiple people have a birthday on {date_text}")
else:
    print("there are no matching birthdays.")

# Run through 100,000 simulations.
print(f"Generating {num_b_days}, random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
# How many simulations had matching brithdays in them
sim_match = 0
for i in range(100_000):
    # Report on the progress every 10,000 simulations.
    if i % 10_000 == 0:
        print(f"{i}, simulations run...")
    birthdays = get_birthdays(num_b_days)
    if get_match(birthdays) != None:
        sim_match += 1
print("100,000 simulations run.")

# Display simulation results.
probability = round(sim_match / 100_000 * 100, 2)
print(
    f"""Out of 100,000 simulations of {num_b_days} people there was a
    matching birthday in that group {sim_match}, times. This means
    that, {num_b_days} people have a {probability} % chance of
    having a matching birthday in their group.
    That's probably more than what you would've thought."""
)
