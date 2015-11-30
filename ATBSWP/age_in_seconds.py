def age_program():
    user_age = input("Enter your Age : ")
    age_in_seconds = int(user_age) * 365 * 24 * 60 * 60
    print("Your age in seconds is {}".format(age_in_seconds))


age_program()
