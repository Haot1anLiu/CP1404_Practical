
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

#When will a ValueError occur?
# When the numerator or denominator of the input is not a number.
#When will a ZeroDivisionError occur?
# when the denominator is entered as 0.
#Could you change the code to avoid the possibility of a ZeroDivisionError?
# yes, to use an if statment.