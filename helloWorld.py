print("Git is awesome")
info_out = input("What is yor name? ")
print(info_out)

# Code to take user input. Numeric vales only otherwise question is repeated.
i=1
while i==1:
    user_age = input("What is your age in years? ")
    if user_age.isnumeric():
        print(f"{info_out} is: {user_age} years old.")
        i=0
    else:
        print("You have not entered a valid number. Please try again.")

