age = 19
isBirthday = False

if age >= 21:
    print("YOU CAN DRINK.")
    if isBirthday:
        print("HAPPY BIRTHDAY, HEERE IS A FREE SHOT!")
elif age >= 18:
    print("YOU CAN COME IN BUT NO DRINKING!")
    if isBirthday:
        print("HAPPY BIRTHDAY, HEERE IS A FREE APPLE JUICE!")
else:
    print("SORRY GO HOME KID!")