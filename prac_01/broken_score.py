score = float(input("Please enter the score:"))

if score <= 100 and score >= 0 :
    if score >= 90 :
        print("excellent")
    elif score >= 50 :
        print("pass")
    else:
        print("bad")
else:
    print("Invalid")