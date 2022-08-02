#This python code converts entered Temperature in Celsius to Fahrenheit

tempC = input("Enter the temperature in Celsius: ")
#convert string to float
tempC = float(tempC)

#convert the temp to Fahrenheit
tempF = (1.8 * tempC) + 32

print(tempC,"celsisus is equal to",tempF, "in FahrenHeit")
