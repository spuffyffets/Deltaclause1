def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Temperature Converter")

    # Get user input for conversion type
    conversion_type = input("Choose conversion type (F to C or C to F): ").upper()

    if conversion_type not in ['F TO C', 'C TO F']:
        print("Invalid conversion type. Please enter 'F TO C' or 'C TO F'.")
        return

    # Get temperature value from the user
    try:
        temperature = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")
        return

    # Perform the conversion
    if conversion_type == 'F TO C':
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to {result:.2f} degrees Celsius.")
    else:
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature} degrees Celsius is equal to {result:.2f} degrees Fahrenheit.")

if __name__ == "__main__":
    main()
