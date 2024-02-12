print("Git is awesome")

# Code to take users first name.
user_name = input("What is your first name? ")
print(user_name)

# Code to take user input. Numeric vales only otherwise question is repeated.
i=1
while i==1:
    user_age = input("What is your age in years? ")
    if user_age.isnumeric():
        print(f"{user_name} is: {user_age} years old.")
        i=0
    else:
        print("You have not entered a valid number. Please try again.")

