print("Welcome to the Goat's Bar.\nLets proceed with some identification.")
ask_name = input("What is your name?")
age_bracket = input("What is your age" + ask_name + "?")
age_bracket = int(age_bracket)
if age_bracket > 21:
    print("Age verified!")
else:
    print("You are not old enough for this")
    exit()
salary_information = input("What is your salary?")
salary_information = int(salary_information)

#This is the salary bracket for client classification
if salary_information < 70000:
    print("You are in group D.\nPlease enjoy your stay!")
else:
    if salary_information < 200000:
        print("You are in group C.\nPlease enjoy your stay!")
    else:
        if salary_information < 800000:
            print("You are in group B.\nPlease enjoy your stay!")
        else:
            if salary_information < 2000000:
                print("You are in group A.\nPlease enjoy your stay!")