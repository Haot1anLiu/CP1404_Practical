def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").upper()
temp = float(input("Enter temperature: "))

if choice == "C":
    print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit.")
elif choice == "F":
    print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius.")
