age = 19
isbirthday = True

if age >= 21:
    print("You are old enough to drink")
    if isbirthday:
            print("You get a free drink")
elif age >= 18:
        print("You are old enough to vote but no drinking")
        if isbirthday:
            print("You get a free shirt")
else:
            print("Sorry Go Home Kid")