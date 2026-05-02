while True:
    f_or_c = input("Enter F or C: ")
    if f_or_c == "F":
        f = float(input("Enter the temperature in F: "))
        c = (f - 32) * 5 / 9
        print(f"{f} Fahrenheit is {c:.2f} degrees Celsius to 2 decimal points.")
    elif f_or_c == "C":
        c = float(input("Enter the temperature in C: "))
        f = (c * 9 / 5) + 32
        print(f"{c} degrees Celsius is {f:.2f} Fahrenheit to 2 decimal points.")
    else:
        print("Invalid input. Please enter F or C.")