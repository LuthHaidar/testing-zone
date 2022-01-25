def celsius_to_fahrenheit(c):
    return ((c/5)*9)+32

def fahrenheit_to_celsius(f):
    return ((f-32)*5)/9

f_or_c = input("Type F for Fahrenheit to Celsius conversion, and C for Celsius to Fahrenheit conversion: ")

deg = int(input("Type in the temperature to be converted: "))

if f_or_c = "F": fahrenheit_to_celsius(deg)
    else if f_or_c = "C": celsius_to_fahrenheit(deg)
    else: pass
